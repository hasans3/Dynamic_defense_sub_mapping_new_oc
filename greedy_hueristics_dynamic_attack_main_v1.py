# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 09:39:04 2017

@author: saqibhasan

DYNAMIC ATTACK GREEDY HUERISTICS

This code is used to identify the transmission lines and its associated protection assembly that cause the worst 
load loss at different stages by using greedy hueristics. It is an extended version of greedy_algorithm.py

"""

def worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
    from compiler.ast import flatten    
#    import greedy_hueristics_dynamic_attack_support
    import dynamic_outage_at_specific_stages_v1
    import maptest_updated_outage_list
    dynamic_initial_outage_temp = [];
    dynamic_initial_outage = [];
    worst_case_dynamic_stage_outage = [];
    temp_worst_case_stage_number = [];
    temp_first_outage = [];
    temp_additional_dynamic_outage = [];
    temp_first_outage_state_vec = [];
    temp_additional_dynamic_outage_state_vec = [];
#    dynamic_stage_outage_list = [];
#    dynamic_temp_load_loss = 0;
#    worst_case_dynamic_stage_outage = [];
#    worst_case_max_load_loss = 0;
#    temp_worst_case_stage_number = 0;
    stage_vector = [1,2,3];
#    static_worst_case_outage, static_worst_case_load_loss = greedy_hueristics_dynamic_attack_support.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget);
    static_worst_case_outage_list = [['Line.tl2122','Line.tl139','Line.tl12','Line.tl939','Line.tl89','Line.tl58','Line.tl87','Line.tl65','Line.tl54','Line.tl34','Line.tl23','Line.tl225','Line.tl2526','Line.tl318','Line.tl1817','Line.tl1727','Line.tl2726','Line.tl1617','Line.tl1516','Line.tl1415','Line.tl414','Line.tl1413','Line.tl1013','Line.tl1011','Line.tl611','Line.tl2628','Line.tl2829','Line.tl2629','Line.tl1624','Line.tl1621','Line.tl67','Line.tl1619','Line.tl2223','Line.tl2423']];    
#    static_worst_case_outage_list = [['Line.tl67', 'Line.tl2122','Line.tl1817']]    
    static_worst_case_outage_list =  list(flatten(static_worst_case_outage_list)) 
    dynamic_initial_outage_stage_vec = [0];
    static_worst_case_load_loss = 66.74;
    worst_case_max_load_loss = static_worst_case_load_loss;
    dynamic_initial_outage_temp.append(static_worst_case_outage_list[0])
    dynamic_initial_outage.append(list(dynamic_initial_outage_temp))
    dynamic_new_outage_list = maptest_updated_outage_list.maptest14bus_test_system(static_worst_case_outage_list, dynamic_initial_outage_temp);
    dynamic_temp_load_loss, first_outage, first_outage_state_vec, additional_dynamic_outage, additional_dynamic_outage_state_vec = dynamic_outage_at_specific_stages_v1.DSS_Python_Interface1(filepath, load_file_name, blackout_criterion, system_name, dynamic_new_outage_list, dynamic_initial_outage_stage_vec,stage_vector);
    if (dynamic_temp_load_loss > worst_case_max_load_loss):
        worst_case_max_load_loss = dynamic_temp_load_loss;
        temp_first_outage = first_outage[0];
        temp_additional_dynamic_outage = additional_dynamic_outage;
        temp_first_outage_state_vec = first_outage_state_vec;
        temp_additional_dynamic_outage_state_vec = additional_dynamic_outage_state_vec;   
    worst_case_dynamic_stage_outage.append(temp_first_outage);
    worst_case_dynamic_stage_outage.append(temp_additional_dynamic_outage);
    temp_worst_case_stage_number.append(temp_first_outage_state_vec);
    temp_worst_case_stage_number.append(temp_additional_dynamic_outage_state_vec);
    print worst_case_max_load_loss
    print worst_case_dynamic_stage_outage;
    print temp_worst_case_stage_number;
#    print 'I am here'

    
worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2);
