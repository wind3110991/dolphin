#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""server.py"""

from wsgiref.simple_server import make_server
from application import my_app

urls = (
    ("/", "index"),
    ("/hello/(.*)", "hello"),
)

class index:
    def GET(self):
        my_app.header('Content-type', 'text/plain')
        return "Welcome To Dolphin's World!\n"

class hello:
    def GET(self, name):
        my_app.header('Content-type', 'text/plain')
        return "Hello %s!\n" % name

wsgiapp = my_app(urls, globals())

if __name__ == '__main__':
    httpd = make_server('localhost', 8000, wsgiapp)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)

    # Respond to requests until process is killed
    httpd.serve_forever()