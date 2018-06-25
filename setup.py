# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:06:56 2018

@author: kdabhadk
"""

import numpy as np
import pandas as pd
import operator


def get_loc(data,index,P):
    #'Gives location of player P at index ''index'' in data'
    
    if index != len(data):
        x = data[index:index+1][P].values[0][0]
        y = data[index:index+1][P].values[0][1]
    
    if not np.isfinite(x):
        x = 6000
        y = 0
    if not np.isfinite(y):
        x=6000
        y=0
    return x,y

def distance(data,index,P1,P2):
    #'Gives distance between players P1 and P2 at index ''index'' in data''
    return np.sqrt((get_loc(data,index,P1)[0]-get_loc(data,index,P2)[0])**2 + (get_loc(data,index,P1)[1]-get_loc(data,index,P2)[1])**2)

def map_player(data,index):
    #'Maps and sorts each player position as distance from sender at the instant of index'
    index = int(index)
    sender = data.sender[index] #id of sender player
    mapp = {}    
    
    if sender < 15:
        for i in range(1,15):
            text = 'P'+str(i)
            player_loc = data.loc[index,text]
            if (np.isfinite(player_loc[0])) and i!=sender:
                mapp[i]=distance(data,index,'P'+str(sender),text)
        
        mapp=sorted(mapp.items(), key=operator.itemgetter(1))
        
        li={}
        
        for i in range(15,29):
            text = 'P'+str(i)
            player_loc = data.loc[index,text]
            if (np.isfinite(player_loc[0])) and i!=sender:
                li[i]=distance(data,index,'P'+str(sender),text)
                
        li=sorted(li.items(), key=operator.itemgetter(1))
        
        mapp.extend(li)
                
    elif sender > 14:
        for i in range(15,29):
            text = 'P'+str(i)
            player_loc = data.loc[index,text]
            if (np.isfinite(player_loc[0])) and i!=sender:
                mapp[i]=distance(data,index,'P'+str(sender),text)
        
        mapp=sorted(mapp.items(), key=operator.itemgetter(1))
        
        li={}
        
        for i in range(1,15):
            text = 'P'+str(i)
            player_loc = data.loc[index,text]
            if (np.isfinite(player_loc[0])) and i!=sender:
                li[i]=distance(data,index,'P'+str(sender),text)
                
        li=sorted(li.items(), key=operator.itemgetter(1))
        
        mapp.extend(li)
            
    return mapp

def make_feature(data,index):
    index = int(index)
    mapp = map_player(data,index)
    receiver = data.receiver[index]
    
    id_list=[]
    dist_list=[]    
    
    for element in mapp:
        dist_list.append(element[1])
        id_list.append(element[0])
        
    x = np.array(dist_list)
       
    y = np.zeros((1,21))
    y[0,id_list.index(receiver)] = 1

    return x,y