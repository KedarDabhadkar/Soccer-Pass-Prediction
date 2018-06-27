# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:56:15 2018

@author: kdabhadk
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from setup import *
from data_transform import *

def plot_instance(data,h):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 20
    fig_size[1] = 10
    
    plt.grid(linestyle='-', linewidth=0.2)
    
    for i in range(1,29):
        text_ = 'P'+str(i)
    
        if i<15:
            if np.isfinite(get_loc(data,h,text_)[0]) and np.isfinite(get_loc(data,h,text_)[1]):
                plt.plot(get_loc(data,h,text_)[0],get_loc(data,h,text_)[1],'ro')            
                plt.text(get_loc(data,h,text_)[0],get_loc(data,h,text_)[1],text_)
        else:
             if np.isfinite(get_loc(data,h,text_)[0]) and np.isfinite(get_loc(data,h,text_)[1]):
                plt.plot(get_loc(data,h,text_)[0],get_loc(data,h,text_)[1],'go')
                plt.text(get_loc(data,h,text_)[0],get_loc(data,h,text_)[1],text_)
                
    sender_x,sender_y = get_loc(data,h,'P'+str(data[h:h+1]['sender'].values[0]))
    receiver_x,receiver_y= get_loc(data,h,'P'+str(data[h:h+1]['receiver'].values[0]))
                
    plt.arrow(sender_x,sender_y,receiver_x-sender_x,receiver_y-sender_y,head_width = 150,length_includes_head=True)
    plt.plot([-5250, 5250],[-3400, -3400],'b-')
    plt.plot([-5250, -5250],[3400, -3400],'b-')
    plt.plot([-5250, 5250],[3400, 3400],'b-')
    plt.plot([5250, 5250],[3400, -3400],'b-')
    
    plt.legend()
#    plt.show()
    data[h:h+1]
    
    