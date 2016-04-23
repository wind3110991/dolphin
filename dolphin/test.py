# import threading

# ctx = threading.local()
# print ctx
# print ctx.clear()
# import Cookie
# import urllib
# m = Cookie.Morsel()
# m.set('name', 'DarkBull', 'DarkBull')
# m['expires'] = 'Fir, 01-Oct-2010 20:00:00 GMT'
# m['domain'] = 'appspot.com'
# cookies =Cookie.SimpleCookie()
# cookie = dict([(k, urllib.unquote(v.value)) for k, v in cookie.iteritems()])
# print cookie
# #print m.output()
# #print m.OutputString()


# import sys
# d = {'1': 'd', '2': 'e'}
# dic = dict([(k, d) for k,v in d.iteritems()])
# print dic


# import socket

# def validip6addr(addr):
# 	try:
# 		socket.inet_pton(socket.AF_INET6, addr)
# 	except (socket.error, AttributeError):
# 		return False

# 	return True

# t_addr = 'aaaa:bbbb:cccc:dddd::s1'
# print validip6addr(t_addr)

import sys, re

class Tews:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return "a is %s, b is %s" % (self.a, self.b)

class Singleton:
	def __new__(cls, t):
		return t
class T(Singleton):
	a = 1

if __name__ == "__main__":
  # t = '127.0.0.1:8000'
  # a = t.split(':',1)
  # g = '127.0.0.1'
  # b = g.split(':',1)
  # print a[0], a[1]
  # if len(b) is 1:
  #   print b[0]
  #   print len(a), len(b)
  ip = '[::32]:88'
  test = re.search(r'^\[([^]]+)\](?::(\d+))?$', ip)
  print test.group(1)


# class Person(object):

#   """Silly Person"""

#   def __new__(cls, name, age):

#     print '__new__ called.'

#     return super(Person, cls).__new__(cls, name, age)

#   def __init__(self, name, age):

#     print '__init__ called.'

#     self.name = name

#     self.age = age

#   def __str__(self):

#     return '<Person: %s(%s)>' % (self.name, self.age)

# if __name__ == '__main__':

#   piglei = Person('piglei', 24)

#   print piglei


# Use this version for Python 2
# import os
# import urllib2
 
# from threading import Thread
 
# ########################################################################
# class DownloadThread(Thread):
#     """
#     A threading example that can download a file
#     """
 
#     #----------------------------------------------------------------------
#     def __init__(self, url, name):
#         """Initialize the thread"""
#         Thread.__init__(self)
#         self.name = name
#         self.url = url
 
#     #----------------------------------------------------------------------
#     def run(self):
#         """Run the thread"""
#         handle = urllib2.urlopen(self.url)
#         fname = os.path.basename(self.url)
#         with open(fname, "wb") as f_handler:
#             while True:
#                 chunk = handle.read(1024)
#                 if not chunk:
#                     break
#                 f_handler.write(chunk)
#         msg = "%s has finished downloading %s!" % (self.name,
#                                                    self.url)
#         print(msg)
 
# #----------------------------------------------------------------------
# def main(urls):
#     """
#     Run the program
#     """
#     for item, url in enumerate(urls):
#         name = "Thread %s" % (item+1)
#         thread = DownloadThread(url, name)
#         thread.start()
 
# if __name__ == "__main__":
#     urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#     main(urls)