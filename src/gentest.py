# -*- coding: utf-8 -*-
import os
import sys
import re
import jinja2

class Gentest:
    """
    generate test file from source file
    """
    
    def __init__(self, sourcefile):
        self.sourcefile = sourcefile
        self.dect_file = "test_"+self.sourcefile

    def write_template(self):
        """
        write template string to test file
        """
        cname = self.sourcefile.split('.')[0]
        ds_conf = {"name" : self.dect_file,
                 "classname" : cname.capitalize()
                }

        TemplateLoader = jinja2.FileSystemLoader(os.path.abspath('../fileTemplate'))
        TemplateEnv = jinja2.Environment(loader=TemplateLoader)
        template = TemplateEnv.get_template('test_config.py')
        dsconf = template.render(ds_conf)
        print(dsconf)

        with open(self.dect_file, 'w') as file:
            file.writelines(dsconf + "\n")

    def append_context(self, context):
        """
        append context to target file
        """
        temp = str()
        for var in context:
            temp = "    def test_" + var + "(self):\n        pass\n\n"
            with open(self.dect_file, 'a') as file:
                file.writelines(temp)

    def search_source(self):
        """
        search source file get function define
        return save dict
        """
        savestr = str()
        with open(self.sourcefile, 'r') as file:
            savestr = file.readlines()

        res = []
        for var in savestr:
            st = var.strip()
            if re.search(r"def", var):
                #print(st.split(' ')[1].split('(')[0] + "\n")
                res.append(st.split(' ')[1].split('(')[0])
        return res

    def excute_test(self):
        """
        excute test file
        """
        cmd = "pytest " + self.dect_file
        res = os.system(cmd)
        if res != 0:
           print("run cmd failed")


     

g = Gentest("config.py")
g.write_template()
context = g.search_source()
g.append_context(context)
g.excute_test()
