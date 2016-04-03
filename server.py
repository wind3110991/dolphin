#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" server.py """

"""服务器启动文件"""

import sys
from dolphin.api.api import *
from dolphin.apps.urls import *
from wsgiref.simple_server import make_server

#Get the port number by administrator
tmp_port = int(sys.argv[1])

#def wsgiapp(environ,start_response):
#    start_response('200 OK', [('Content-type', 'text/html')])
#    return '<h1>Hello,Welcome to Dolphin!</h1>'

#Testing by Wind
my_app.header('Content-type', 'text/plain')
wsgiapp = my_app(urls, globals())

if __name__ == '__main__':
    httpd = make_server('localhost', tmp_port, wsgiapp)
    #Testing by Wind
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    print "Serving HTTTP on port %s...." % tmp_port

    # Respond to requests until process is killed
    # Listening to the HTTP request
    httpd.serve_forever()

class WSGIApplication(object):
    def __init__(self, document_root=None, **kw):
        pass

    # 添加一个URL定义:
    def add_url(self, func):
        pass

    # 添加一个Interceptor定义:
    def add_interceptor(self, func):
        pass

    # 设置TemplateEngine:
    @property
    def template_engine(self):
        pass

    @template_engine.setter
    def template_engine(self, engine):
        pass

    # 返回WSGI处理函数:
    def get_wsgi_application(self):
        def wsgi(env, start_response):
            pass
        return wsgi

    # 开发模式下直接启动服务器:
    def run(self, port=9000, host='127.0.0.1'):
        server = make_server(host, port, self.get_wsgi_application())
        server.serve_forever()