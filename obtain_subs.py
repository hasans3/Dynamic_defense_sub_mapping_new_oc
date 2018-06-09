# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:51:58 2018

@author: saqibhasan

This code is used to obtain the substations corresponding to the protection assemblies associated with the respective transmission lines
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range, w_outage):
    
#    from  more_itertools import unique_everseen
    from compiler.ast import flatten
#    valueset = ['Line.tl12', 'Line.tl23', 'Line.tl1011', 'Line.tl1213', 'Line.tl25', 'Line.tl34', 'Line.tl24', 'Line.tl47', 'Line.tl15', 'Line.tl914', 'Line.tl49', 'Line.tl612', 'Line.tl1314', 'Line.tl910', 'Line.tl611', 'Line.tl79', 'Line.tl78', 'Line.tl45', 'Line.tl56', 'Line.tl613'];
#    contingency_range = 1;
    valueset = [];
    subs = {};
    w_outage = list(flatten(w_outage))
#    transmission_line_impedance = [45,49,43,92,38,54];
#    transmission_line_impedance = [12,40,57,35,35,35,44,57,54,39,74,17,42,21,34,8,28];
# -------------- Open and read the text file and convert the content into a list ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()
#    print valueset
#    for item in w_outage:
#        flag = 1
#        for keys in valueset:
#            if item in valueset[keys] and flag == 1:
#                subs[keys] = [item] 
#                flag = 0
##                w_outage.remove(item)
#    print subs
#    return subs
    for keys in valueset:
        temp_key_values = valueset[keys]
        for item in w_outage:
            if item in temp_key_values:
                subs[item] = keys
#    print subs
    return subs
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", 0, 1, [['Line.tl1213', 'Line.tl117', 'Line.tl56', 'Line.tl4445', 'Line.tl910', 'Line.tl115']]);