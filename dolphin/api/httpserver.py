#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" httpserver.py """

""" 定义http服务器的内核 """

import urllib
from dolphin.apps.urls import *
from wsgiref.simple_server import make_server

class WSGIApplication:
    headers = []

    def __init__(self, urls=(), fvars={}):
        self._urls = urls
        self._fvars = fvars
        self._status = '200 OK'

    # def __call__(self, environ, start_response):
    #     del self.headers[:] # 在每次作出响应前，清空上一次的headers
    #     result = self._delegate(environ)
    #     start_response(self._status, self.headers)

    #     # 将返回值result（字符串 或者 字符串列表）转换为迭代对象
    #     if isinstance(result, basestring):
    #         return iter([result])
    #     else:
    #         return iter(result)

    # 返回WSGI处理函数:
    def get_wsgi_application(self):
        def wsgi(environ, start_response):
            del self.headers[:] # 在每次作出响应前，清空上一次的headers
            result = self._delegate(environ)
            start_response(self._status, self.headers)

            # 将返回值result（字符串 或者 字符串列表）转换为迭代对象
            if isinstance(result, basestring):
                return iter([result])
            else:
                return iter(result)
        return wsgi
    def _delegate(self, environ):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        for pattern, name in self._urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                # pass the matched groups as arguments to the function
                args = m.groups()
                funcname = method.upper() # 方法名大写（如GET、POST）
                klass = self._fvars.get(name) # 根据字符串名称查找类对象
                if hasattr(klass, funcname):
                    func = getattr(klass, funcname)
                    return func(klass(), *args)

        return self._notfound()

    def _notfound(self):
        self.status = '404 Not Found'
        self.header('Content-type', 'text/plain')
        return "Sorry, your request url is not found\n"

    # 该类方法用来通过调用为类定义一个header
    @classmethod
    def header(cls, name, value):
        cls.headers.append((name, value))

    # 添加一个URL定义:
    def add_url(self, func):
        pass

    # 添加一个Interceptor定义:
    def add_interceptor(self, func):
        pass

    # 设置TemplateEngine－－模版引擎:
    @property
    def template_engine(self):
        pass

    @template_engine.setter
    def template_engine(self, engine):
        pass

    # 开发模式下直接启动服务器:
    def run(self, port, host):
        #server = make_server(host, port, self.get_wsgi_application())
        server = make_server(host, port, self.get_wsgi_application())
        sa = server.socket.getsockname()
        print 'http://{0}:{1}/'.format(*sa)
        print "Serving HTTTP on port %s...." % port
        server.serve_forever()