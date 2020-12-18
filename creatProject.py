#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import fire
import src.MyLog as mylog
import src.controler as control

basedir = os.getcwd()
log = mylog.get_log()


class Comands(object):
    """Main commands ...."""
    def init(self, projectName, buildPlan):
        """ List data dir ...."""
        # projectName = sys.argv[3]
        # buildPlan = sys.argv[2]
        con = control.Controler(basedir, projectName)

        log.info('-----------load buildPlan.yaml------------')
        if buildPlan == "cc":
            planfile = "cc_plan.yaml"

        if buildPlan == "py":
            planfile = "py_plan.yaml"

        if buildPlan == "golang":
            planfile = "go_plan.yaml"

        data = con.get_yaml_data(basedir + "/" + control.Ptdir + "/" + "py_plan.yaml")

        # reflex
        collection = data.get("main_process")
        reflex_data = collection[0]
        data1 = collection[1]
        # print(str(reflex_data.get("reflex")))
        for var in reflex_data.get("reflex"):
            res = str(type(var))
            # print(type(var))
            try:
                if res=="<class 'str'>":
                    command_act = getattr(con, var)
                    command_act()

                if res=="<class 'dict'>":
                    key = list(var.keys())[0]
                    # print("key is:", key)
                    command_act = getattr(con, key)
                    # print(var.get(key).__len__())
                    if var.get(key).__len__() ==1:
                        # print(type(var.get(key)[0]))
                        # print(var.get(key)[0])
                        # print(data1.get("data"))
                        if var.get(key)[0] == "data1":
                            command_act(data1.get("data"))
                            # print("key is 1")

                    if var.get(key).__len__() ==2:
                        if var.get(key)[0] == "data1" and var.get(key)[1] == "projectName":
                            command_act(data1.get("data"), projectName)
                            # print("key is 2")
            except TypeError:
                try:
                    print("TypeError")
                except TypeError:
                    print("worng")

    def tarin(self):
        """
        print tarin process
        """
        log.info("tarin process .....")

    def result(self):
        """
        print result
        """
    def score(self):
        """
        print score
        """

    def log(self):
        """
        print current log
        """
        os.chdir("logs")
        log.info("logs....")

    def test(self):
        """
        test process
        """


if __name__ == '__main__':
    fire.Fire(Comands)
