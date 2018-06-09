# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 11:28:57 2017

@author: saqibhasan

DYNAMIC ATTACK GREEDY HUERISTICS

This code is used to identify the transmission lines and its associated protection assembly that cause the worst 
load loss at different stages by using greedy hueristics. It is an extended version of greedy_algorithm.py

TO BE ADDED IN THE CODE
Need to add static worst case outage as the worst case attack in case no dynamic outage results in more
load loss.

"""

def worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
    from compiler.ast import flatten    
#    import greedy_hueristics_dynamic_attack_support
    import dynamic_outage_at_specific_stages_v2_testing
    import first_max_load_loss_cascade_algorithm
#    import maptest_updated_outage_list
    import maptest_updated_outage_list_v2_testing
    dynamic_initial_outage_temp = [];
    temp_dynamic_outage = [];
    temp_dynamic_outage_vec = [];
    temp_worst_dynamic_outage = [];
    temp_worst_dynamic_outage_vec = [];
    stage_vector = [1,2,3];
    static_worst_case_outage_list, static_worst_case_load_loss = first_max_load_loss_cascade_algorithm.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name);
#    static_worst_case_outage_list = [['Line.tl67']];    
#    static_worst_case_outage_list = [['Line.tl67', 'Line.tl2122','Line.tl1817']]    
    static_worst_case_outage_list =  list(flatten(static_worst_case_outage_list)) 
    dynamic_initial_outage_stage_vec = [0];
    temp_dynamic_initial_outage_stage_vec = dynamic_initial_outage_stage_vec;
#    static_worst_case_load_loss = 66.74;
    worst_case_max_load_loss = static_worst_case_load_loss;
    dynamic_initial_outage_temp.append(static_worst_case_outage_list[0])
    for k in range(0,(budget-1)):
#        temp_worst_dynamic_outage = [];
        dynamic_new_outage_list = maptest_updated_outage_list_v2_testing.maptest14bus_test_system(comp_filename, dynamic_initial_outage_temp, start_range, contingency_range);
        dynamic_temp_max_load_loss, temp_dynamic_outage, temp_dynamic_outage_vec = dynamic_outage_at_specific_stages_v2_testing.DSS_Python_Interface1(filepath, load_file_name, blackout_criterion, system_name, dynamic_new_outage_list, temp_dynamic_initial_outage_stage_vec,stage_vector);
        dynamic_initial_outage_temp = temp_dynamic_outage;
        temp_dynamic_initial_outage_stage_vec = temp_dynamic_outage_vec;
        print dynamic_temp_max_load_loss
        print temp_dynamic_outage
        print temp_dynamic_outage_vec
        if (dynamic_temp_max_load_loss > worst_case_max_load_loss):
            worst_case_max_load_loss = dynamic_temp_max_load_loss;
            temp_worst_dynamic_outage = temp_dynamic_outage;
            temp_worst_dynamic_outage_vec = temp_dynamic_outage_vec;
    print '================================================================================================='
    print 'Worst Case Load Loss: %f' %worst_case_max_load_loss
    print 'Worst Case Outage: %s' %temp_worst_dynamic_outage
    print 'Worst Case Outage Vector: %s' %temp_worst_dynamic_outage_vec;
    print '================================================================================================='
    
worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml',2);
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 3);
#worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2);    
