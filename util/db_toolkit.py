# coding:utf-8
#@Time    :2019/3/31 15:44
import pymysql
from entity.plan import *
class MySQLTool:
    def __init__(self):
        self.db = pymysql.connect("localhost","root","root","email" )

    def _find_item_by_id(self,imp_id):
        return None

    def _plan_insert(self,new_plan):
        pass
    def _plandata_insert(self,new_plan):
        pass
    def store(self,new_item):
        if isinstance(new_item, Plan):
            self._plan_insert(new_item)
        elif isinstance(new_item,PlanData):
            self._plandata_insert(new_item)
        else:
            print("type error")