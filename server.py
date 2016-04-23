#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" server.py """

""" web服务启动文件 """

import sys, os
from dolphin.apps.urls import *
from dolphin.api.api import *
from dolphin.api.httpserver import *

localhost = '127.0.0.1'
#def wsgiapp(environ,start_response):
#    start_response('200 OK', [('Content-type', 'text/html')])
#    return '<h1>Hello,Welcome to Dolphin!</h1>'

WSGIApplication.header('Content-type', 'text/plain')
wsgiapp = WSGIApplication(urls, globals())

if __name__ == '__main__':
    #Get the port number by administrator
    tmp_port = int(sys.argv[1])

    # Respond to requests until process is killed
    # Listening to the HTTP request
    wsgiapp.run(tmp_port, localhost)