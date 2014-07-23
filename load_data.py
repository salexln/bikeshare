# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:04:07 2014

@author: Goren
"""
import csv
import numpy as np

class loader:
    """Loads data """
    def __init__(self,csv):
        #hard coded magic
        self.csv='D:\\code\\python\\bikeshare\\data\\{}.csv'.format(csv)

    def read(self):
        """ Reads csv into a numpy structure"""
        #read csv
        infile=open(self.csv,"rb")
        reader=csv.reader(infile,delimiter=',')
        next(reader, None)#skip the headers
        x=list(reader)
        return np.array(x).astype('float')

#for tests
if __name__=='__main__':
    train_loader=loader('train_processed')
    train=train_loader.read()
    holiday=train[:,2]
    rentals=train[:,11]
    holiday_rentals = np.ma.masked_where(holiday==1,rentals).sum()
    non_holiday_rentals = np.ma.masked_where(holiday==0,rentals).sum()
    print train
    #print train[:,[6,11]]