# -*- coding: utf-8 -*-
import os
import sys
import jinja2 as jin


class Config:
    """configure class"""
    def __init__(self, confile):
        self.confile = confile

    def write_conf(self, value):
        """
        write context to configure file
        """
        with open(self.confile, 'w') as file:
            print(file.writelines(value))

    def read_keyfile(self, key):
        """
        read key from value file
        """
        with open(self.confile, 'r') as file:
            print(file.read(key))


    def update_conf(self, key, value):
        """
        update configure file
        """
