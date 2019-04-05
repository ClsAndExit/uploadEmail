# -*- coding: utf-8 -*-
#@Time    :2019/3/31 15:45
from util.conf_toolkit import ConfigManager
ConfigManager.init_class("config/emailFile.conf")
local_file_path = ConfigManager.get_local_resource_folder()
import pandas as pd
def download_to_local_file(file_path):
    pass

def is_file_of_excel(file_name):
    if len(file_name.split('.')) >= 1:
        file_type = file_name.split('.')[1]
        return (file_type == 'xls') or (file_type == 'xlsx')
    else:return False
def del_file_as_excel(file_data):
    for data in file_data:
        f = open(local_file_path+data, "rb")
        realdata = pd.read_excel(f)

        print(realdata)
        pass