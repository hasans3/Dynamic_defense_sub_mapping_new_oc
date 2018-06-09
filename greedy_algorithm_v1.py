# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:22:18 2017

@author: saqibhasan

This code is used to identify the transmission lines and its associated protection assembly that cause the worst load loss by using 
greedy hueristics. It is an extended version of greedy_algorithm.py

"""

def greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
    import cascade_algorithm
    import maptest_new_outage_list
    import cascade_algorithm_reduced_outages
    import time
    tot_exe_time_start = time.time()
    temp_max_loadloss = 0;
    worst_case_outage = [];
    max_load_loss_outage, max_loadloss = cascade_algorithm.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name);
#    print max_load_loss_outage
    temp_max_loadloss = max_loadloss;
    worst_case_outage = max_load_loss_outage;  
    for k in range(0, (budget-1)):
        new_outage_list = maptest_new_outage_list.maptest14bus_test_system(comp_filename, start_range, contingency_range, max_load_loss_outage);
#        print new_outage_list
        max_load_loss_outage, max_loadloss = cascade_algorithm_reduced_outages.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, new_outage_list);
        if (max_loadloss > temp_max_loadloss):
            temp_max_loadloss = max_loadloss;
            worst_case_outage = max_load_loss_outage;
    tot_exe_time_end = time.time()
    tot_exe_time = (tot_exe_time_end - tot_exe_time_start)
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print 'Worst case outage: %s' %worst_case_outage
    print 'Worst case loadloss: %s' %temp_max_loadloss
    print 'Total execution time in seconds: %s' %tot_exe_time
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

#greedy_hueristics("'G:\saqib\open DSS\opendss_matlab_interface\ieee9bus_system.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\component_data_heuristics.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\Load_data_with_reactive_load.txt", 0, 1, 40, 'wscc9bus_system_test_N-1.xml', 2);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 3);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 4);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base_testing.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1_testing.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 3);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing2.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_test.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_test.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_test1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_test1.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
