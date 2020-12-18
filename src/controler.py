# -*- coding: utf-8 -*-
import os
import sys
import shutil
import yaml
import src.MyLog as mylog

# project template files directory
Ptdir = "buildPlan"
Ftdir = "fileTemplate"

log = mylog.get_log()


class Controler:
    """
    mainly control function
    """
    def __init__(self, basePath, projectname):
        self.basePath = basePath
        self.projectname = projectname
        pass

    def get_yaml_data(self, yaml_file):
        """
        read yaml
        """
        # 打开yaml文件
        file = open(yaml_file, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()

        # print(file_data)
        # print("类型：", type(file_data))

        # 将字符串转化为字典或列表
        log.info("***转化yaml数据为字典或列表***")
        data = yaml.safe_load(file_data)
        log.info(data)
        log.info("类型：", type(data))
        return data

    def info(self):
        # display information
        log.info('-----------display info  ---------------')
        log.info('To create project template: createProject your projectname')
        log.info('It consist file:')
        log.info('dir: contributed,data,modle,src,test,tmp,util')
        log.info('files:__init__.py,LICENSE.md,README.md,\
        requirements.txt,setup.py,main.py')

    # create function
    def create_Function(self, data):
        log.info('-----------create directory---------------')
        os.mkdir(self.projectname)
        log.info('create project dir: ' + self.projectname)

        os.chdir(self.projectname)
        log.info("chdir: " + os.getcwd())
        # setup git
        self.SetupGit()

        for i in data.get("dir_Array"):
            os.mkdir(i)
            log.info('create subdir: ' + str(i))

        for j in data.get("file_Array"):
            res = open(j, 'a')
            res.close()
            log.info('create files: ' + str(j))

        # create childarray of src
        os.chdir('src')
        log.info("chdir: " + os.getcwd())
        for l in data.get("child_Array"):
            os.mkdir(l)
            log.info('create subdir: ' + str(l))

    def copy_File(self, data):
        """
        copy project Template File and directory to project directory
        """
        log.info('------------copy file---------------------')
        source = self.basePath + "/" + Ftdir + "/"
        targetPath = self.basePath + "/" + self.projectname
        # copy file
        filename =  data.get("copy_File")[0].get("file").get("filename")
        copypath =  data.get("copy_File")[0].get("file").get("path")
        try:
            shutil.copyfile(source + filename,
                        targetPath + "/" + copypath + "/" + filename)
        except IOError as e:
            log.error("Unable to copy file. %s" % e)
            exit(1)
        except:
            log.error("system error", sys.exc_info())
            exit(1)
        log.info("File copy done!")

        # copy directory
        dirname = data.get("copy_File")[1].get("dirs").get("dir_name")
        path = data.get("copy_File")[1].get("dirs").get("path")
        try:
            shutil.copytree(source +dirname, targetPath + "/" + path + "/" + dirname)
        except IOError as e:
            log.error("Unable to copy directory. %s" % e)
            exit(1)
        except:
            log.error("Unexpected error:", sys.exc_info())
            exit(1)

        log.info("Dir copy done!")

    def SetupGit(self):
        # setup git
        res = os.system("git init")
        if res != 0:
            log.error("run 'git init' failed")

    def BuildProject(self, data):
        """
        build template project
        """
        log.info('------------build project------------------')
        if data.get("buildProj") == None:
            log.error("Item buildProj is not in configure file!")
        else:
            buildcmd = data.get("buildProj")[0].get("compile")
            res = os.system(buildcmd)
            if res !=0:
                log.error("run 'build project' failed")

        # run project
        runcmd = data.get("buildProj")[0].get("run")
        res = os.system(runcmd)
        if res != 0:
            log.error("run 'run project' failed")

    def write_file(self, data):
        """
        write workspace Build file
        """
        log.info('------------write file---------------------')
        # read yaml
        if data.get("writeBuildFile") == 0:
            log.error("Item writeBuildFile is not in configure file!")
