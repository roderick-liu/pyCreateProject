# -*- coding: utf-8 -*-
import yaml
import os

class Yaml:
    def __init__(self, filename):
        """
        init Yaml object
        """
        self.data = yaml.safe_load(filename)
    
        
    

