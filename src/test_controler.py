#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from controler import Controler

if __name__ == '__main__':
    pytest.main("-s test_controler.py")

class Test_Controler:
   def setup(self):
       print("----setup")

   def test_copy_file(self):
       """
       test copy_file
       """
       c = Controler(".","testDemo")
       tdata = {'copy_File': [{'file': {'filename': 'main.py', 'path': ''}}, {'dirs': {'dir_name': 'util', 'path': 'src'}}]}
       c.copy_File(tdata)
       if 1==1:
          print("test_copy_file")
        

