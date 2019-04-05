# -*- coding: utf-8 -*-
#@Time    :2019/3/31 15:44
import pymysql
from util import file_toolkit
from util.conf_toolkit import ConfigManager
from entity.item import Item
class MySQLTool:
    def __init__(self):
        self.db = pymysql.connect("localhost","email","root","root" )

    def _find_item_by_id(self,imp_id):
        return None

    def store(self,new_item):
        if not isinstance(new_item, Item):
            raise ValueError("parameter is in Error type")