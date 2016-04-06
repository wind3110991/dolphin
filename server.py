#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" server.py """

"""服务器启动文件"""

import sys
from dolphin.apps.urls import *
from dolphin.api.api import *
from dolphin.api.httpserver import *

#def wsgiapp(environ,start_response):
#    start_response('200 OK', [('Content-type', 'text/html')])
#    return '<h1>Hello,Welcome to Dolphin!</h1>'

#Testing by Wind
WSGIApplication.header('Content-type', 'text/plain')
wsgiapp = WSGIApplication(urls, globals())

if __name__ == '__main__':
    #Get the port number by administrator
    tmp_port = int(sys.argv[1])

    # Respond to requests until process is killed
    # Listening to the HTTP request
    ##httpd.serve_forever()
    wsgiapp.run(tmp_port, '127.0.0.1')