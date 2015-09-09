#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" libs.py """

""" import some API if needed """

import sys
import time
import os
import urllib
from wsgiref.simple_server import make_server

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