# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:53:58 2017

@author: saqibhasan
"""

def maptest14bus_test_system(comp_filename, start_range, contingency_range):
    
# To generate all possible combinations itertools is needed
#    import itertools
#    a_list = [];
#    a_list_2 = [];
#    a_l = [];
    CMB = [];
    CMB_new = [];
    temp_valueset = [];
    new_valueset = []
#    valueset = [['Line.tl23'], ['Line.tl1011'], ['Line.tl1213'], ['Line.tl25'], ['Line.tl34'], ['Line.tl24'], ['Line.tl47'], ['Line.tl15'], ['Line.tl914'], ['Line.tl49'], ['Line.tl612'], ['Line.tl1314'], ['Line.tl910'], ['Line.tl611'], ['Line.tl79'], ['Line.tl78'], ['Line.tl45'], ['Line.tl56'], ['Line.tl613']];
    valueset = ['Line.tl1011', 'Line.tl1213', 'Line.tl25', 'Line.tl34', 'Line.tl24', 'Line.tl15', 'Line.tl914', 'Line.tl612', 'Line.tl1314', 'Line.tl910', 'Line.tl611', 'Line.tl79', 'Line.tl78', 'Line.tl45', 'Line.tl613'];
    new_valueset = [valueset[i:i+1] for i in range(0, len(valueset), 1)]
#    print new_valueset
#    contingency_range = 1;
#    valueset =[];
#    transmission_line_impedance = [45,49,43,92,38,54];
#    transmission_line_impedance = [12,40,57,35,35,35,44,57,54,39,74,17,42,21,34,8,28];
    iter_max_load_loss_outage = [['Line.tl12', 'Line.tl23']]
# -------------- Open and read the text file and convert the content into a list ----------------    
#    data_file = open(comp_filename, 'r'); 
#    line_data = data_file.readline();
#    valueset = eval(line_data);
#    data_file.close()
#    print len(valueset)
    for i in range(0, len(valueset)):
        temp_valueset = new_valueset[i];
#        print temp_valueset
        temp_iter_max_load_loss_outage = iter_max_load_loss_outage[0];
#        print temp_iter_max_load_loss_outage
        iter_temp_comb = temp_valueset + temp_iter_max_load_loss_outage;
#        print iter_temp_comb
        CMB.append(iter_temp_comb)
    CMB_new.append(CMB)
    return CMB_new
#    print CMB
    
#    list1=['a','b','c']
#    list2=[['e','f','g']]
#    a1 = [list(x + tuple(list2[0])) for x in itertools.combinations(list1,1)]
#    print a1
#    for i in range(0, len(list1)):
#        a = list1[i];
#        b = list2[0];
#        c = list(a) + b
#        a_l.append(c)
#    print a_l
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt",0,1);
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\component_data_heuristics.txt",1,2);
