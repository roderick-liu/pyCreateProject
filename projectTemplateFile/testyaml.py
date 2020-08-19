#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os


def get_yaml_data(yaml_file):
    """
    read yaml
    """
    # 打开yaml文件
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    
    print(file_data)
    print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data)
    print(data)
    print("类型：", type(data))
    return data

current_path=os.path.abspath(".")
yaml_path=os.path.join(current_path,"buildPlan.yaml")
print('--------------------',yaml_path)
get_yaml_data(yaml_path)


# yaml文件中含多个文档时，分别获取文档中数据
def get_yaml_load_all(yaml_file):
    #打开文件
    file=open(yaml_file,'r',encoding='utf-8')
    file_data=file.read()
    file.close()

    all_data=yaml.load_all(file_data,Loader=yaml.FullLoader)
    for data in all_data:
        print('data-----',data)

# current_path=os.path.abspath(".")
# yaml_path=os.path.join(current_path,"configall.yaml")
# get_yaml_load_all(yaml_path)


#生成yaml文档
def generate_yaml_doc(yaml_file):
    py_ob={"school":"zhang",
           "students":['a','b']}
    file=open(yaml_file,'w',encoding='utf-8')
    yaml.dump(py_ob,file)
    file.close()

# current_path=os.path.abspath(".")
# yaml_path=os.path.join(current_path,"generate.yaml")
# generate_yaml_doc(yaml_path)
