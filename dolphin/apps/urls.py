#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""urls.py"""

"""添加app的url访问路径"""

import re
from dolphin.apps.views import *

#在这里添加需要的url规则
urls = (
    ("/", "index"),
    ("/hello/(.*)", "hello"),
    ("/test/(.*)", "test")
)

class my_app:
    headers = []

    def __init__(self, urls=(), fvars={}):
        self._urls = urls
        self._fvars = fvars
        self._status = '200 OK'

    def __call__(self, environ, start_response):
        del self.headers[:] # 在每次作出响应前，清空上一次的headers
        result = self._delegate(environ)
        start_response(self._status, self.headers)

        # 将返回值result（字符串 或者 字符串列表）转换为迭代对象
        if isinstance(result, basestring):
            return iter([result])
        else:
            return iter(result)

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
        return "Not Found\n"

    @classmethod
    def header(cls, name, value):
        cls.headers.append((name, value))


""" Example End """
