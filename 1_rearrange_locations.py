# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:06:56 2018

@author: kdabhadk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator
import time

file = pd.read_csv('passes.csv')

data = pd.DataFrame()
data['sender'] = file['sender_id']
data['receiver'] = file['receiver_id']
data['time_start'] = file['time_start']
data['time_end'] = file['time_end']
for i in range(1,29):
    data['P'+str(i)] = list(zip(file['x_'+str(i)],file['y_'+str(i)]))
    
list_ = [i for i in np.arange(len(data))]

list_ = [i for i in np.arange(len(data))]
data = data.reindex(np.array(list_))

data.to_csv('1_rearranged.csv')