# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:10:06 2017

@author: saqibhasan

DYNAMIC ATTACK GREEDY HUERISTICS

This code is used to identify the transmission lines and its associated protection assembly that cause the worst 
load loss at different stages by using greedy hueristics. It also considers the order of the attack(s).
It considers the entire number of components in the network and their ordering.
It is an extended version of greedy_algorithm.py

"""

def worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
    from compiler.ast import flatten    
#    import greedy_hueristics_dynamic_attack_support
    import dynamic_outage_at_specific_stages_v2_testing
    import maptest_updated_outage_list_dynamic_attack_with_order_v1_testing
    import maptest_testing
    import time
    total_dynamic_ordering_exe_start_time = time.time();
    dynamic_initial_outage_temp = [];
    static_greedy_worst_case_outage = [];
    static_greedy_worst_case_load_loss = [];
    temp_dynamic_outage = [];
    temp_dynamic_outage_vec = [];
    temp_worst_dynamic_outage = [];
    temp_worst_dynamic_outage_vec = [];
    stage_vector = [1,2,3];
    static_greedy_worst_case_load_loss = 0;
#    static_greedy_worst_case_outage, static_greedy_worst_case_load_loss = greedy_hueristics_dynamic_attack_support.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget);
    static_greedy_worst_case_outage = maptest_testing.maptest14bus_test_system(comp_filename, start_range, contingency_range);   
    static_greedy_worst_case_outage =  list(flatten(static_greedy_worst_case_outage)); 
#    static_greedy_worst_case_outage = ['Line.tl2122', 'Line.tl67', 'Line.tl2629'];
#    static_greedy_worst_case_load_loss = 70.74;
    worst_case_max_load_loss = static_greedy_worst_case_load_loss;
    temp_worst_dynamic_outage = static_greedy_worst_case_outage;
    for item in static_greedy_worst_case_outage:
        temp_worst_dynamic_outage_vec.append(0);
    for t in range(0, len(static_greedy_worst_case_outage)):
        print '================================================================================================='
        print 'ORDER NUMER %d FROM SELECTION' %t;
        dynamic_initial_outage_temp = [];
        dynamic_initial_outage_stage_vec = [0];
        temp_dynamic_initial_outage_stage_vec = dynamic_initial_outage_stage_vec;
        dynamic_initial_outage_temp.append(static_greedy_worst_case_outage[t]);
    #    print static_greedy_worst_case_load_loss
        for k in range(0, (budget-1)):
            dynamic_new_outage_list = maptest_updated_outage_list_dynamic_attack_with_order_v1_testing.maptest14bus_test_system(static_greedy_worst_case_outage, dynamic_initial_outage_temp);
    #        print dynamic_new_outage_list
            dynamic_temp_max_load_loss, temp_dynamic_outage, temp_dynamic_outage_vec = dynamic_outage_at_specific_stages_v2_testing.DSS_Python_Interface1(filepath, load_file_name, blackout_criterion, system_name, dynamic_new_outage_list, temp_dynamic_initial_outage_stage_vec,stage_vector);   
            dynamic_initial_outage_temp = temp_dynamic_outage;
            temp_dynamic_initial_outage_stage_vec = temp_dynamic_outage_vec;
    #        print dynamic_temp_max_load_loss
    #        print temp_dynamic_outage
    #        print temp_dynamic_outage_vec
            if (dynamic_temp_max_load_loss >= worst_case_max_load_loss):
                worst_case_max_load_loss = dynamic_temp_max_load_loss;
                temp_worst_dynamic_outage = temp_dynamic_outage;
                temp_worst_dynamic_outage_vec = temp_dynamic_outage_vec; 
        print '================================================================================================='
    total_dynamic_ordering_exe_end_time = time.time();
    total_dynamic_ordering_exe_time = (total_dynamic_ordering_exe_end_time - total_dynamic_ordering_exe_start_time);
    print '================================================================================================='
    print 'Worst Case Load Loss (in percent): %f' %worst_case_max_load_loss
    print 'Worst Case Outage: %s' %temp_worst_dynamic_outage
    print 'Worst Case Outage Vector (representing attacks at individual stages): %s' %temp_worst_dynamic_outage_vec
    print 'Total Execution Time in Seconds: %s' %total_dynamic_ordering_exe_time
    print '================================================================================================='
    
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml',4);
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 2);
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 6);    
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing1.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 6);    
worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing2.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 3);    
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base_testing.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1_testing.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2);
#--------------------------------------------- only for testing ------------------------------------------------------------

#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base_results.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1_results.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 4);
