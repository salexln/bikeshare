# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:04:07 2014

@author: Goren
"""
import csv
import numpy as np

class train_loader:
    """Loads data """
    TestcasesRatio=0.1
    
    def __init__(self,csv):
        #hard coded magic
        self.csv='D:\\code\\python\\bikeshare\\data\\{}.csv'.format(csv)
        self.read()

    def read(self):
        """ Reads csv into a numpy structure"""
        #read csv
        infile=open(self.csv,"rb")
        reader=csv.reader(infile,delimiter=',')
        next(reader, None)#skip the headers
        x=list(reader)
        self.data=np.array(x).astype('float')
        
    def training_data(self,data_cols,target_col):
        test_size=int(round(self.data.shape[0]*self.TestcasesRatio))
        X= self.data[0:-test_size,data_cols]
        y=self.data[0:-test_size,target_col]
        return (X,y)
        
    def test_data(self,data_cols,target_col):
        test_size=int(round(self.data.shape[0]*self.TestcasesRatio))
        X= self.data[-test_size:,data_cols]
        y=self.data[-test_size:,target_col]
        return (X,y)

#for tests
if __name__=='__main__':
    loader=train_loader('train_processed')
    (X,y)=loader.training_data(range(9),9)
    print X
    #print train[:,[6,11]]