#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import sys
import shutil
import yaml

# project template files directory
ptdir = "projectTemplateFile"

logging.basicConfig(level = logging.INFO,format =
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
basedir = os.getcwd()


def get_yaml_data(yaml_file):
    """
    read yaml
    """
    # 打开yaml文件
    #print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # print(file_data)
    # print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.safe_load(file_data)
    print(data)
    print("类型：", type(data))
    return data


def info():
    # display information
    print('To create project template: createProject your projectname')
    print('It consist file:')
    print('dir: contributed,data,modle,src,test,tmp,util')
    print('files:__init__.py,LICENSE.md,README.md,\
    requirements.txt,setup.py,main.py')


# create function
def createFun(projectname, data):
    os.mkdir(projectname)
    logger.info('create project dir: ' + projectname)

    os.chdir(projectname)
    print("chdir: " + os.getcwd())
    # setup git
    setupGit()

    for i in data.get("dirArray"):
        os.mkdir(i)
        logger.info('create subdir ' + str(i))

    for j in data.get("fileArray"):
        res = open(j ,'a')
        res.close()
        logger.info('create files' + str(j))

    # create childarray of src
    os.chdir('src')
    print("chdir: " + os.getcwd())
    for l in data.get("childArray"):
        os.mkdir(l)
        logging.info('create subdir' + str(l))


def copyFile(data, target):
    """
    copy project Template File and directory to project directory
    """
    source = basedir + "/" + ptdir + "/"
    targetPath = basedir + "/" + target
    # copy file
    try:
        shutil.copy(source + data.get("copyFile")[0].get("file").get("filename"),targetPath + "/" + data.get("copyFile")[0].get("file").get("path"))
    except IOError as e:
        logger.error("Unable to copy file. %s" % e)
        exit(1)
    except:
        logger.error("Unexpected error:", sys.exc_info())
        exit(1)

    # copy directory
    dirname = data.get("copyFile")[1].get("dirs").get("dirname")
    path = data.get("copyFile")[1].get("dirs").get("path")
    try:
        shutil.copytree(source +dirname, targetPath + "/" + path + "/" + dirname)
    except IOError as e:
        logger.error("Unable to copy directory. %s" % e)
        exit(1)
    except:
        logger.error("Unexpected error:", sys.exc_info())
        exit(1)

    logger.info("File copy done!")


def setupGit():
    # setup git
    res = os.system("git init")
    if res != 0:
        print("run 'git init' failed")


if __name__ == '__main__':
    projectName = sys.argv[1]
    logger.info('-----------print information of system----')
    info()

    logger.info('-----------load buildPlan.yaml------------')
    data = get_yaml_data(basedir + "/" + ptdir + "/" + "buildPlan.yaml")
    print(data.get("copyFile")[0].get("file").get("path"))

    logger.info('-----------create directory---------------')
    createFun(projectName, data)

    logger.info('------------copy file---------------------')
    copyFile(data, projectName)
