#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" server.py """

""" write down any config if needed """

reload(sys)
sys.setdefaultencoding('utf-8')

__all__ = [

]

# add forbidden clients into lists who hava no right to share your server
forbidden_ip = [

]

#database connection

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'db_test'
}

Database.connect(**db_config)