#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''web.py'''

'''提供web操作支持的相关API'''

__all__ = [
    #Operations
    "config",
    "debug",
    "HTTPError",

    "OK", #200
    "Redirect", #301
    "BadRequest", #400
    "Forbidden", #403
    "NotFound", #404
    "InternalError" #500
]

from dolphin.api.tools import *
import sys, cgi, Cookie, pprint, urlparse, urllib, urllib2
import threading

# 全局ThreadLocal对象：
"""Threading有一个非常特别的类local。一旦在主线程实例化了一个local，它会一直活在主线程中，
并且又主线程启动的子线程调用这个local实例时，它的值将会保存在相应的子线程的字典中。
目的在于：在当前线程保存一个全局值，并且各自线程互不干扰
"""
ctx = context = threading.local()

# 处理状态码
def status_code(status, data=None, cls_name=None, doc_str=None):
    if data is None:
        data = status.split(" ", 1)[1]

    cls_name = status.split(" ", 1)[1].replace(' ', '') #例如"304 Not Modified" -> "NotModified"
    doc_str = "%s status" % status

    def __init__(self, data=data, headers={}):
        HTTPError.__init__(self, status, headers, data)

    # 返回一个状态码对应的类型，附带着可读性强的docstring
    return type(cls_name, (HTTPError, object), {
            '__doc__': doc_str,
            '__init__': __init__
        })

ok = OK = status_code("200 OK", data="")
created = Created = status_code("201 Created")
accepted = Accepted = status_code("202 Accepted")
nocontent = NoContent = status_code("204 No Content")

#重定向：指向一个新的url
class Redirect(HTTPError):
    def __init__(self, url, status="301 Moved Permanently", absolute):
        #absolute：是否绝对路径
"""
        import urlparse 演示urlparse效果
        url = "https://www.google.com.hk:8080/home/search;12432?newwi.1.9.serpuc#1234"  
        r = urlparse.urlparse(url)
        print r
        ParseResult(scheme='https', netloc='www.google.com.hk:8080', 
         path='/home/search', params='12432', query='newwi.1.9.serpuc', fragment='1234')
"""        
        new_loc = urlparse.urljoin(ctx.path, url) #urljoin(base, url)

        #该loc为/开头，如果是相对路径的话，
        if new_loc.startswith('/'):
            if absolute:
                home = ctx.realhome
            else:
                home = ctx.home
            new_loc = home + new_loc
        
        headers = {
            'Content-Type': 'text/html',
            'Location': new_loc
        }
        HTTPError.__init__(self, status, headers, "")

redirect = Redirect

class Found(Redirect):
    def __init__(self, url, absolute):
        Redirect.__init__(self, url, "302 Found", True)

found = Found

# 400 Bad Request
class BadRequest(HTTPError):
    """`400 Bad Request` error."""
    msg = "bad request"
    def __init__(self, message=None):
        status = "400 Bad Request"
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, msg)

badrequest = BadRequest

# 403 Forbidden
class Forbidden(HTTPError):
    msg = "403 Forbidden"
    def __init__(self, msg):
        status "403"
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, self.msg)

forbidden = Forbidden

# 500 Internal Error
class InternalError(HTTPError):
    msg = "500 InternalError Server Error"

    def __init__(self, msg):
        status = '500 Internal Server Error'
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, self.msg)

internalerror = InternalError
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

# HTTP错误类:
class HttpError(Exception):
    def __init__(self, status, headers={}, data):
        ctx.status = status
        for x, y in headers.items():
            header(x, y)
        self.data = data
        Exception.__init__(self, status)

# 检测response中的header是否合法
def header(hdr, value, unique=False):
    hdr, value = safestr(hdr), safestr(value)
    # protection against HTTP response splitting attack
    if '\n' in hdr or '\r' in hdr or '\n' in value or '\r' in value:
        raise ValueError,
        
    if unique is True:
        for h, v in ctx.headers:
            if h.lower() == hdr.lower(): return

    # 若符合条件，则在context中headers添加header和value信息
    ctx.headers.append((hdr, value))

def set_cookie(name, value, expires='', domain=None, secure=False, http_only=False, path=None):
    """
        Abstract a key/value pair, which has some RFC 2109 attributes. (from Python Doc)
    """
    morsel = Cookie.Morsel()
    name = safestr(name)
    value = safestr(value)
    morsel.set(name, value, urllib.quote(value)) # Morsel.set(key, value, coded_value)name, value, urllib.quote(value)
    # 假如该cookie已经过期，那么赋值为大负数(???)
    if expires < 0:
        expires = -100000000
    morsel['expires'] = expires
    morsel['path'] = path or ctx.homepath + '/'
    if domain:
        morsel['domain'] = domain
    if secure:
        morsel['secure'] = secure
    value = morsel.OutputString() #区别于output()，缺少"Set-Cookie:"
    if http_only:
        value += '; httponly'
    headers('Set-Cookie', value)

def decode_cookie(v):
    try:
        # First try plain ASCII encoding
        return unicode(v, 'us-ascii')
    except UnicodeError:
        # Then try UTF-8, and if that fails, ISO8859
        try:
            return unicode(v, 'utf-8')
        except UnicodeError:
            return unicode(v, 'iso8859', 'ignore')

def parse_cookie(http_cookie):
    r""" Cookie String Format is divided by ';'
        eg: name=DarkBull; Domain=appspot.com; expires=Fir, 01-Oct-2010 20:00:00 GMT
    """
    # 检查cookie中是否包括双引号
    if '"' in http_cookie:
        cookie = Cookie.SimpleCookie()
        try:
            # 解析字符串为Cookie数据
            cookie.load(http_cookie)
        except Cookie.CookieError:
            for attr_val in http_cookie.split(';'):
                try:
                    cookie.load(attr_val)
                except Cookie.CookieError:
                    print "Cookie Parsing Failed"
        cookies = dict([(k, urllib.unquote(v.value)) for k, v in cookie.iteritems()])
    else:
        cookie = {}
        for key_val in http_cookie.split('.'):
            key_val = key_value.split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                cookies[key.strip()] = urllib.unquote(value.strip())
    return cookies

# * 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。 **用来处理传递任意个有名字的参数，这些参数用dict来访问。
def cookies(*requireds, **defaults):
    r"""RFC2965 Cookie"""
    if _unicode.get("_unicode") is True:
        defaults['_unicode'] = decode_cookie

    if '_parse_cookie' not in ctx:
        http_cookie = ctx.env.get("HTTP_COOKIE", "")
        ctx._parsed_cookies = parse_cookies(http_cookie)
    try:
        return storify(ctx._parsed_cookies, *requireds, **defaults)
    except KeyError:
        badrequest()
        raise StopIteration

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