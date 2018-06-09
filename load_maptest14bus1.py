# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 11:01:35 2016

@author: saqibhasan

This is the function to calcaulate the load loss given a contingency.
It is used in cascade_algorithm.py

"""

def load_maptest14bus(load_file_name, load_loss):
    
#    keyset1 = {'Load.load1': 21.7,'Load.load2': 7.6,'Load.load3': 11.2,'Load.load4': 6.1,'Load.load5': 13.8,'Load.load6': 3.5,'Load.load7': 14.9,'Load.load8': 9,'Load.load9': 16.6,'Load.load10': 47.8,'Load.load11': 94.2};
# -------------- Open and read the text file and convert the content into a dictionary ----------------
#    keyset1 = {'Load.load2': (7600,1600),'Load.load5': (13800,5800),'Load.load8': (9000,5800),'Load.load9': (29500,16600),'Load.load3': (11200,7500),'Load.load11': (94200,19100),'Load.load4': (6100,1600),'Load.load6': (3500,1800),'Load.load1': (21700,12700),'Load.load10': (47800,-3900),'Load.load7': (14900,5000)}
    file_data = open(load_file_name, 'r')
    data = file_data.readline();
    keyset1 = eval(data);
    file_data.close()
    #load_loss = ['Load.load2','Load.load5'];
    load_loss1 = load_loss;
    import math
    Total_system_load = 0.0;
    load_loss_values = [];
    amount_load_loss= 0.0;
# ----------------- Calculating the total system load ------------------
    values = keyset1.values();
    for i in range(0 , len(values)):
        c = 0.0;
        for j in range(0,2):
            a = values[i][j];
            b = a*a;
            c = c+b;
        d = math.sqrt(c);
        Total_system_load = Total_system_load + d;
# ----------------- Getting the values of the keys from dictionary ------------------
#    load_loss_size = len(load_loss1);
    load_loss_size = len(load_loss1);
    for i in range(0, load_loss_size):
        load_loss_values.append(keyset1[load_loss1[i]]);
#    print load_loss_values
# ----------------- Calculating the total load loss ------------------
    for i in range(0, len(load_loss_values)):
        c = 0.0;
        for j in range(0,2):
            a = load_loss_values[i][j];
#            print a
            b = a*a;
            c = c+b;
        d = math.sqrt(c);
        amount_load_loss = amount_load_loss + d;
#        print amount_load_loss
    return (Total_system_load, amount_load_loss);
    
#load_maptest14bus("G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", load_loss);