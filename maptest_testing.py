# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:21:26 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range):
    
# To generate all possible combinations itertools is needed
    import itertools
    from  more_itertools import unique_everseen
    from compiler.ast import flatten
    cmb = [];
#    valueset = ['Line.tl12', 'Line.tl23', 'Line.tl1011', 'Line.tl1213', 'Line.tl25', 'Line.tl34', 'Line.tl24', 'Line.tl47', 'Line.tl15', 'Line.tl914', 'Line.tl49', 'Line.tl612', 'Line.tl1314', 'Line.tl910', 'Line.tl611', 'Line.tl79', 'Line.tl78', 'Line.tl45', 'Line.tl56', 'Line.tl613'];
#    contingency_range = 1;
    valueset = [];
    valueset1 = [];
#    transmission_line_impedance = [45,49,43,92,38,54];
#    transmission_line_impedance = [12,40,57,35,35,35,44,57,54,39,74,17,42,21,34,8,28];
# -------------- Open and read the text file and convert the content into a list ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()
#    print valueset
    for keys in valueset:
        valueset1.append(valueset[keys])
#        valueset1.append(list(unique_everseen(valueset[keys])))
    valueset1 = list(unique_everseen(flatten(valueset1)))
#    print valueset1
#    print len(valueset1)
# ------------- Generate all the possible combinations from the list ------------- 
    for i in range(start_range, contingency_range):
        comb=[];
        for j in itertools.combinations(valueset1, i+1):
            comb.append(list(j));
            #print comb
        cmb.append(comb);
#    print cmb
    return cmb;
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", 0,1);