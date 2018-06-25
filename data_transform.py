# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:41:54 2018

@author: kdabhadk
"""

import numpy as np
import pandas as pd
import operator
from setup import *

def transform(file):
    #Transforms the columns in the original file to include player locations as tuple

    data = pd.DataFrame()
    data['sender'] = file['sender_id']
    data['receiver'] = file['receiver_id']
    data['time_start'] = file['time_start']
    data['time_end'] = file['time_end']

    for i in range(1,29):
        data['P'+str(i)] = list(zip(file['x_'+str(i)],file['y_'+str(i)]))

    list_ = [i for i in np.arange(len(data))]

    data = data.reindex(np.array(list_))

    return data

def change_type(col):
    #Changes types of all location columns from string to tuple
    newcol=[]
    #Input col as series
    for element in col:
        ele = element.replace(' ',',')
        ele = ele.replace('(',',')
        ele = ele.replace(')',',')
        ele = ele.split(',')
        newcol.append((float(ele[1]),float(ele[3])))
    return newcol

def make_feature(data,index,all_players=True):
    index = int(index)
    mapp = map_player(data,index,all_players)
    receiver = data.receiver[index]
    
    id_list=[]
    dist_list=[]    
    
    for element in mapp:
        dist_list.append(element[1])
        id_list.append(element[0])
        
    x = np.array(dist_list)
    
    if all_players:       
        y = np.zeros((1,21))
    else:
        y = np.zeros((1,10))
    y[0,id_list.index(receiver)] = 1

    return x,y