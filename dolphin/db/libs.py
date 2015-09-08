import sys, time, os, urllib

try:
    import datetime
except ImportError:
    datetime = None

try: set
except NameError:
    from sets import Set as set
    
from utils import *

try:
	print "some API"
    #from webapi import debug, config
except:
    import sys
    debug = sys.stderr
    config = storage()