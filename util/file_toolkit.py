# -*- coding: utf-8 -*-
#@Time    :2019/3/31 15:45
import pandas as pd
from util.conf_toolkit import ConfigManager
ConfigManager.init_class("config/emailFile.conf")
local_file_path = ConfigManager.get_local_resource_folder()
def download_to_local_file(filename,data):
    att_file = open(local_file_path + filename, 'wb')
    att_file.write(data)  # 保存附件
    att_file.close()

def is_file_of_excel(file_name):
    file_type = file_name.split('.')[1]
    return (file_type == 'xls') or (file_type == 'xlsx')


def del_file_as_excel(file_data):
    for data in file_data:
        f = open(local_file_path+data, "rb")
        realdata = pd.read_excel(f)

        print(realdata)
        pass