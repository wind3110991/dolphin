#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" networks.py """

""" 网络部分处理以及验证模块 """

from dolphin.api.tools import *
import re
import socket
import datetime, time

# 判断addr是否为ipv6地址
def validip6addr(addr):
	try:
		socket.inet_pton(socket.AF_INET6, addr)
	except (socket.error, AttributeError):
		return False
		print "Invalid Ipv6 Address"
	return True

def validipaddr(addr):
	try:
		octets = oct_num = address.split('.')
		if len(oct_num) is not 4:
			return False
		for x in octets:
			if not (0 <= int(x) <= 255):
				return False
	except ValueError:
		return False
	return True

def validipport(port):
	try:
		if not (0 <= int(port) <= 65535):
			return False
	except ValueError:
		return False
	return True

def validip(ip, defaultaddr="0.0.0.0", defaultport=8000):
	r"""    Returns `(ip_address, port)` from string `ip_addr_port`
    >>> validip('1.2.3.4')
    ('1.2.3.4', 8000)
    >>> validip('80')
    ('0.0.0.0', 80)
    >>> validip('192.168.0.1:85')
    ('192.168.0.1', 85)
    >>> validip('::')
    ('::', 8000)
    >>> validip('[::]:88')
    ('::', 88)
    >>> validip('[::1]:80')
    ('::1', 80)"""
    
	addr = defaultaddr
	port = defaultport
	#检测是否正确的ipv6地址
	with_port = re.search(r'^\[([^]]+)\](?::(\d+))?$', ip) # check for [ipv6]:port  eg: [::2]:8080
	if with_port:
		tmp_addr = with_port.group(1)
		tmp_port = int(with_port.group(2))
		if validip6addr(ip):
			addr = tmp_addr
			port = tmp_port
	elif validip6addr(ip):
		# 如果是不带port的ipv6型地址
		addr = ip
		return (addr, port)
	else:
		raise ValueError, ':'.join(ip) + ' is not a valid IP address/port'
	#检测ip地址为ipv4的情况
	tup = ip.split(':', 1)
	if validipaddr(ip):
		if len(tup) == 1:
			addr = tup[0]
			return (addr, port)
		elif len(tup) == 2:
			addr = tup[0]
			port = int(tup[1])
			return (addr, port)
	else:
		raise ValueError, ':'.join(ip) + ' is not a valid IP address/port'

def httpdate(date):
	r"""
		%a 星期几的简写
		%A 星期几的全称
		%b 月分的简写
		%B 月份的全称
		%c 标准的日期的时间串
		%C 年份的后两位数字
		%d 十进制表示的每月的第几天
		%D 月/天/年
		%e 在两字符域中，十进制表示的每月的第几天
		%F 年-月-日
		%g 年份的后两位数字，使用基于周的年
		%G 年分，使用基于周的年
		%h 简写的月份名
		%H 24小时制的小时
		%I 12小时制的小时
		%j 十进制表示的每年的第几天
		%m 十进制表示的月份
		%M 十时制表示的分钟数
		%n 新行符
		%p 本地的AM或PM的等价显示
		%r 12小时的时间
		%R 显示小时和分钟：hh:mm
		%S 十进制的秒数
		%t 水平制表符
		%T 显示时分秒：hh:mm:ss
		%u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
		%U 第年的第几周，把星期日做为第一天（值从0到53）
		%V 每年的第几周，使用基于周的年
		%w 十进制表示的星期几（值从0到6，星期天为0）
		%W 每年的第几周，把星期一做为第一天（值从0到53）
		%x 标准的日期串
		%X 标准的时间串
		%y 不带世纪的十进制年份（值从0到99）
		%Y 带世纪部分的十制年份
		%z，%Z 时区名称，如果不能得到时区名称则返回空字符。
		%% 百分号
	"""
	if date is not None:
		# Header Request中的date格式：Date:Thu, 21 Apr 2016 16:30:35 GMT
		return date.strftime("%a, %d %b %Y %H:%M:%S GMT")
	else:
		return None

# 日期数据解析
def parsehttpdate(string_):
    try:
        t = time.strptime(string_, "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        return None
    return datetime.datetime(*t[:6])

def urlquote(url_str):
    if url_str is None:
    	return ''
    if not isinstance(url_str, unicode):
    	val = str(url_str)
    else:
    	val = val.encode('utf-8')
    return urllib.quote(val)

# html转义
def htmlquote(text):
    r"""
    将符号文本转义为html文本
        >>> htmlquote(u"<'&\">")
        u'&lt;&#39;&amp;&quot;&gt;'
    """
    text = text.replace(u"&", u"&amp;") # Must be done first!
    text = text.replace(u"<", u"&lt;")
    text = text.replace(u">", u"&gt;")
    text = text.replace(u"'", u"&#39;")
    text = text.replace(u'"', u"&quot;")
    return text

# html反转义
def htmlunquote(text):
    r"""
    将html文本反转义为符号文本
        >>> htmlunquote(u'&lt;&#39;&amp;&quot;&gt;')
        u'<\'&">'
    """
    text = text.replace(u"&quot;", u'"')
    text = text.replace(u"&#39;", u"'")
    text = text.replace(u"&gt;", u">")
    text = text.replace(u"&lt;", u"<")
    text = text.replace(u"&amp;", u"&") # Must be done last!
    return text

def websecurity(_str):
	"""
	    >>> websecurity("<'&\">")
        u'&lt;&#39;&amp;&quot;&gt;'
        >>> websecurity(None)
        u''
        >>> websecurity(u'\u203d')
        u'\u203d'
        >>> websecurity('\xe2\x80\xbd')
        u'\u203d'
	"""
	if _str is None:
		return u''
    elif isinstance(_str, str):
        val = _str.decode('utf-8')
    elif not isinstance(_str, unicode):
        val = unicode(_str)
        
    return htmlquote(val)