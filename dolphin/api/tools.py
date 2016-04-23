#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" tools.py """

""" 提供框架所必要的工具 """
from wsgiref.simple_server import make_server
import sys, time, os
import urllib
try:
    import datetime
except ImportError:
    datetime = None

try: set

except NameError:
    from sets import Set as set
    
#from utils import *

try:
	pass
    #from webapi import debug, config
except:
    import sys
    debug = sys.stderr
    config = storage()

#字符串安全检测
def safestr(obj, encoding='utf-8'):
    r"""
    Converts any given object to utf-8 encoded string. 
    
        >>> safestr('hello')
        'hello'
        >>> safestr(u'\u1234')
        '\xe1\x88\xb4'
        >>> safestr(2)
        '2'
    """
    if isinstance(obj, unicode):
        return obj.encode(encoding)
    elif isinstance(obj, str):
        return obj
    elif hasattr(obj, 'next'): # iterator
        return itertools.imap(safestr, obj)
    else:
        return str(obj)

def safeunicode(obj, encoding='utf-8'):
    r"""
    Converts any given object to unicode string.
    
        >>> safeunicode('hello')
        u'hello'
        >>> safeunicode(2)
        u'2'
        >>> safeunicode('\xe1\x88\xb4')
        u'\u1234'
    """
    t = type(obj)
    if t is unicode:
        return obj
    elif t is str:
        return obj.decode(encoding)
    elif t in [int, float, bool]:
        return unicode(obj)
    elif hasattr(obj, '__unicode__') or isinstance(obj, unicode):
        return unicode(obj)
    else:
        return str(obj).decode(encoding)
# for backward-compatibility


utf8 = safestr