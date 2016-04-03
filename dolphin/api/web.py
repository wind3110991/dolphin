#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''web.py'''

'''提供web操作支持'''

# 全局ThreadLocal对象：
ctx = threading.local()

# HTTP错误类:
class HttpError(Exception):
    pass

# request对象:
class Request(object):
    # 根据key返回value:
    def get(self, key, default=None):
        pass

    # 返回key-value的dict:
    def input(self):
        pass

    # 返回URL的path:
    @property
    def path_info(self):
        pass

    # 返回HTTP Headers:
    @property
    def headers(self):
        pass

    # 根据key返回Cookie value:
    def cookie(self, name, default=None):
        pass

#这里定义了response对象:
class Response(object):
    # 设置header:
    def set_header(self, key, value):
        pass

    # 设置Cookie:
    def set_cookie(self, name, value, max_age=None, expires=None, path='/'):
        pass

    # 设置status状态码:
    @property
    def status(self):
        pass
    @status.setter
    def status(self, value):
        pass

# 定义GET方法:
def get(path):
    pass

# 定义POST方法:
def post(path):
    pass

# 定义模板:
def view(path):
    pass

# 定义拦截器:
def interceptor(pattern):
    pass

# 定义模板引擎:
class TemplateEngine(object):
    def __call__(self, path, model):
        pass

# 缺省使用jinja2模版框架:
# class Jinja2TemplateEngine(TemplateEngine):
#     def __init__(self, templ_dir, **kw):
#         from jinja2 import Environment, FileSystemLoader
#         self._env = Environment(loader=FileSystemLoader(templ_dir), **kw)

#     def __call__(self, path, model):
#         return self._env.get_template(path).render(**model).encode('utf-8')