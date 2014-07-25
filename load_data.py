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
        self.readcsv(csv_name,shuffle)
        
    def readcsv (self,csv_name,shuffle=False):
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
        
    def scale(self,cols,scale_min=0,scale_max=0):
        """
        Scales the columns such that:
        1 = maximal value of each column
        0 = minimal value of each column
        """
        for col in cols:
            col_min=scale_min
            col_max=scale_max
            #if scale bounds aren't specified or invalid:
            if (scale_min>=scale_max):
                col_min=self.data[:,col].min()
                col_max=self.data[:,col].max()
            #do the scaling
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

class bikeshare_loader(train_loader):
    def __init__(self):
        self.readcsv('train_processed',True)
    def preprocess(self):
        """Preprocessing for the bikeshare problem"""
        self.scale([1,4,8])#season(1-4),weather(1-4),humidity,windspeed
        self.scale([5,6,7],0,100)#temp,atemp,humidity
        self.data[:,0]=(1/24)*(self.data[:,0]%24)#time of day
        
    
#for tests
if __name__=='__main__':
    loader=bikeshare_loader()
    loader.preprocess()
    (X,y)=loader.training_data(range(9),9)
    print X[:,0]
    #print train[:,[6,11]]