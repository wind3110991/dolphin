#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views.py'''

'''客户可以根据需求编写app逻辑代码'''

class index:
    def GET(self):
        #my_app.header('Content-type', 'text/plain')
        return "Welcome To Dolphin's World!\n"

class hello:
    def GET(self, name):
        #my_app.header('Content-type', 'text/plain')
        return "Hello %s!\n" % name

class test:
    def GET(self, name):
        #my_app.header('Content-type', 'text/plain')
        return "<h1>Test the environment of Dolphin</h1>"