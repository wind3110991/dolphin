#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""urls.py"""

"""添加app的url访问路径"""

import re
from dolphin.apps.views import *

#在这里添加需要的url规则
urls = (
    ("/", "index"),
    ("/hello/(.*)", "hello"),
    ("/test/(.*)", "test")
)
