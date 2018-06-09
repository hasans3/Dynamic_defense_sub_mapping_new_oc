# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:38:43 2017

@author: saqibhasan

This code is used to identify the transmission lines and its associated protection assembly that cause the worst load loss by using 
greedy hueristics.

"""

def greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
#    import maptest_testing
    import cascade_algorithm
    import maptest_new_outage_list
    import cascade_algorithm_reduced_outages
    temp_max_loadloss = 0;
    max_load_loss_outage, max_loadloss = cascade_algorithm.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name);
    print max_load_loss_outage
    temp_max_loadloss = max_loadloss;
    for k in range(0, (budget-1)):
        new_outage_list = maptest_new_outage_list.maptest14bus_test_system(comp_filename, start_range, contingency_range, max_load_loss_outage);
        print new_outage_list
        max_load_loss_outage, max_loadloss = cascade_algorithm_reduced_outages.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, new_outage_list);
#    if (new_max_loadloss > temp_max_loadloss):
#        temp_max_loadloss = new_max_loadloss
greedy_hueristics("'G:\saqib\open DSS\opendss_matlab_interface\ieee9bus_system.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\component_data_heuristics.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\Load_data_with_reactive_load.txt", 0, 1, 40, 'wscc9bus_system_test_N-1.xml', 3);