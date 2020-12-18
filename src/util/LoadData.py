import numpy as np
import pandas as pd
import os
import sympy as sm
import json
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LoadData:

    ldf = pd.DataFrame()

    def __init__(self):
        """
        init local dataframe:ldf
        """
    def generate_csv(self, filename):
        """
        generate data file in data directory
        """
        try:
            f = os.open(filename,os.O_RDONLY)
            logger.info('file existed')
        except Exception as e:
            logger.warning(e)
            f = os.open(filename, os.O_CREAT)
            return os.path.abspath(filename)

    def write_csv(self,filename, data):
        """
        write data to csv
        """
        df = pd.DataFrame(data)
        df.to_csv(filename)

    def generateData(self,listfun):
        """
        input list of function
        generate data by function
        save data to pandas
        """

        # read list of function
        # sympy generate data
        for i in listfun:
            temp = str(i)
            logging.info(temp)
            # caluate data
        # generate dataframe
        merge_dt_dict= {'date':date_list,
                        'update':update_list,
                        'serverip':serverip_list}
        data_df = pd.DataFrame(merge_dt_dict)
        logger.info('data_df' +data_df.columns)

        # write data to dataframe
        data_df.insert(2,'dkdk',[2,3,4])
        return data_df

    def readData(self):
        """
        load data from csv
        """
        filePath = self.getDataPath()
        if filePath.endswith('csv') :
            df = pd.read_csv(filePath)
            if df.__le__ == 0:
                logger.info('load csv failed') 
            return df

        if filePath.endswith('json'):
            return  pd.read_json(filePath)

    def getDataPath(self):
        """
        return data path
        """
        datadir = "data"
        file = os.listdir("data")
        return  datadir + "/" + file[0]

 
