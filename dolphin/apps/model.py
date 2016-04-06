# -*- coding: utf-8 -*-

""" model.py """

""" Data ORM """

import sys
import os
from dolphin.db.db import Model, Field


""" Example """
class ModelName(Model):
	db_table = 'table name'
	id = Field()
	gateway = Field()
	subnetmask = Field()
	netdevicename = Field()
	vlan = Field()
	min = Field()
	max = Field()