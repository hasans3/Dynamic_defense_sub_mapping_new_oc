# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 12:06:26 2017

@author: saqibhasan

This function provides the updated list after greedily picking up an attack from the given list obtained
from static greedy attack.

"""
from copy import deepcopy
def maptest14bus_test_system(comp_name_list, max_load_loss_contingency):
#    import maptest_testing
    from compiler.ast import flatten    
# To generate all possible combinations itertools is needed
    CMB = [];
    CMB_new = [];
    temp_valueset = [];
    new_valueset = []
    valueset_new = []
    iter_max_load_loss_outage = [];
#    valueset = maptest_testing.maptest14bus_test_system(comp_filename, start_range, contingency_range);
    valueset = deepcopy(comp_name_list);
    valueset_new = valueset;
    print valueset;
#    valueset_new = initial_static_worst_case_list;
#    valueset_new = list(flatten(valueset))
    iter_max_load_loss_outage.append(max_load_loss_contingency);
#    iter_max_load_loss_outage = [['Line.tl12', 'Line.tl1011']]
#    print iter_max_load_loss_outage
    max_load_loss_outage = iter_max_load_loss_outage
    max_load_loss_outage = list(flatten(max_load_loss_outage))
#    print len(iter_max_load_loss_outage)
#    print len(valueset[0])
#    print max_load_loss_outage[0]
#    print len(max_load_loss_outage)
    for elem in range(0, len(max_load_loss_outage)):
#        print max_load_loss_outage[elem]
        valueset_new.remove(max_load_loss_outage[elem])
    new_valueset = [valueset_new[i:i+1] for i in range(0, len(valueset_new), 1)]    
    for i in range(0, len(new_valueset)):
        temp_valueset = new_valueset[i];
#        print temp_valueset
        temp_iter_max_load_loss_outage = iter_max_load_loss_outage[0];
#        print temp_iter_max_load_loss_outage
        iter_temp_comb = temp_iter_max_load_loss_outage + temp_valueset;
#        print iter_temp_comb
        CMB.append(iter_temp_comb)
    CMB_new.append(CMB)
    print CMB_new
    return CMB_new
    
#maptest14bus_test_system(['Line.tl2122', 'Line.tl67', 'Line.tl2629'], ['Line.tl67']);
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", ['Line.tl2122'], 0, 1);
