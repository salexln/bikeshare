# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:04:07 2014

@author: Goren
"""
import csv
import os
import numpy as np
import random

class train_loader:
    """Loads data """
    TestcasesRatio=0.1
    
    def __init__(self,csv_name,shuffle=False):
        """Load the data from the csv file"""
        csv_file=os.getcwd()+'\\data\\{}.csv'.format(csv_name)
        #read csv
        infile=open(csv_file,"rb")
        reader=csv.reader(infile,delimiter=',')
        next(reader, None)#skip the headers
        x=list(reader)
        if (shuffle):
            random.shuffle(x)
        self.data=np.array(x).astype('float')
        
    def scale(self,cols):
        """
        Scales the columns such that:
        1 = maximal value of each column
        0 = minimal value of each column
        """
        for col in cols:
            col_min=self.data[:,col].min()
            col_max=self.data[:,col].max()
            self.data[:,col]=(self.data[:,col]-col_min)/(col_max-col_min)
    def training_data(self,data_cols,target_col):
        """
            returns a partial list of (1-TestcasesRatio) percent of the data
            for training purposes
            and splits the input data into data and target
        """
        test_size=int(round(self.data.shape[0]*self.TestcasesRatio))
        X= self.data[0:-test_size,data_cols]
        y=self.data[0:-test_size,target_col]
        return (X,y)
        
    def test_data(self,data_cols,target_col):
        """
            returns a partial list of TestcasesRatio percent of the data
            for the test set
            and splits the input data into data and target
        """
        test_size=int(round(self.data.shape[0]*self.TestcasesRatio))
        X= self.data[-test_size:,data_cols]
        y=self.data[-test_size:,target_col]
        return (X,y)

#for tests
if __name__=='__main__':
    loader=train_loader('train_processed')
    loader.scale([5])
    (X,y)=loader.training_data(range(9),9)
    print X[:,5].max()
    #print train[:,[6,11]]