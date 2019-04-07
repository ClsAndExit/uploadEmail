# coding:utf-8
#@Time    :2019/3/31 15:45
import pandas as pd
import xlrd
import json
from entity.plan import *
from util.str_toolkit import get_md5_id_from_str
from util.db_toolkit import MySQLTool
from util.conf_toolkit import ConfigManager
mysqltool = MySQLTool()
ConfigManager.init_class("../config/emailFile.conf")
local_file_path = ConfigManager.get_local_resource_folder()

def formatPlan(lines,uuid):
    plan = Plan()
    plandata = PlanData()

    plan.plan_company =lines[0][0]
    plan.plan_number =lines[1][2]
    #xldate_as_tuple第二个参数有两种取值，0或者1，0是以1900-01-01为基准的日期，而1是1904-01-01为基准的日期.
    #此处选用参数 0  ,返回值是一个元组，所以还需要格式化一下
    plan.plan_produceDate = xlrd.xldate.xldate_as_datetime(lines[1][10], 0).strftime('%Y/%m/%d %H:%M:%S')
    plan.plan_uuid =uuid
    print(json.dumps(plan))
    length = len(lines)

    for i in range(4,length-1):
        line = lines[i]
        #保证关联ID相同
        plandata.plan_uuid = uuid
        pass

def formatProduction_steel(lines ,uuid):
    pass

def formatItem(lists):
    uuid_str = str(lists[0][0][0]) + str(lists[0][1][2]) + str(lists[0][1][-1])
    uuid = get_md5_id_from_str(uuid_str)
    formatPlan(lists[0],uuid)
    formatProduction_steel(lists[1],uuid)


def download_to_local_file(filename,data):
    att_file = open(local_file_path + filename, 'wb')
    att_file.write(data)  # 保存附件
    att_file.close()

def is_file_of_excel(file_name):
    file_type = file_name.split('.')[1]
    return (file_type == 'xls') or (file_type == 'xlsx')


def read_file(file_data):
    for data in file_data:
        data = xlrd.open_workbook(local_file_path+data)
        sheet_names = data.sheet_names()

        #用来存储所有的sheet
        table_dict = list()
        for sheet in sheet_names:
            #用来存储一个sheet中的所有行
            line_dict = list()
            table = data.sheet_by_name(sheet)
            nrows = table.nrows
            ncols = table.ncols
            colspan = {}
            if table.merged_cells:
                for item in table.merged_cells:
                    for row in range(item[0], item[1]):
                        for col in range(item[2], item[3]):
                            # 合并单元格的首格是有值的，所以在这里进行了去重
                            if (row, col) != (item[0], item[2]):
                                colspan.update({(row, col): (item[0], item[2])})

            for i in range(0,nrows):
                row = []
                for j in range(ncols):
                    # 假如碰见合并的单元格坐标，取合并的首格的值即可
                    if colspan.get((i, j)):
                        row.append(table.cell_value(*colspan.get((i, j))))
                    else:
                        row.append(table.cell_value(i, j))
                line_dict.append(row)
            table_dict.append(line_dict)
        formatItem(table_dict)

if __name__ == "__main__":
    read_file(["计划管理模板1.xlsx"])