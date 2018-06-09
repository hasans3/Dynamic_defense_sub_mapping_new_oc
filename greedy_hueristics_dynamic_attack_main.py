# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 15:04:36 2017

@author: saqibhasan

DYNAMIC ATTACK GREEDY HUERISTICS

This code is used to identify the transmission lines and its associated protection assembly that cause the worst 
load loss at different stages by using greedy hueristics. It is an extended version of greedy_algorithm.py

"""

def worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget):
    from compiler.ast import flatten    
    import greedy_hueristics_dynamic_attack_support
    import dynamic_outage_at_specific_stages
#    import maptest_updated_outage_list
    dynamic_initial_outage_temp = [];
    dynamic_initial_outage = [];
    dynamic_stage_outage_list = [];
    dynamic_temp_load_loss = 0;
    worst_case_dynamic_stage_outage = [];
    worst_case_max_load_loss = 0;
    temp_worst_case_stage_number = 0;
    stage_vector = [1,2,3];
#    static_worst_case_outage, static_worst_case_load_loss = greedy_hueristics_dynamic_attack_support.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget);
    static_worst_case_outage = [['Line.tl67', 'Line.tl2122']]    
    static_worst_case_outage =  list(flatten(static_worst_case_outage))  
#    worst_case_max_load_loss = static_worst_case_load_loss;
    for i in range(0,len(static_worst_case_outage)):
        if (i == 0):
            dynamic_initial_outage_temp.append(static_worst_case_outage[i])
            dynamic_initial_outage.append(list(dynamic_initial_outage_temp))
        else:
            dynamic_stage_outage_list.append(static_worst_case_outage[i])
    print "Dynamic Initial Outage: %s" %dynamic_initial_outage
    print "Dynamic Stage Outage List: %s" %dynamic_stage_outage_list
    for k in range(0, len(dynamic_stage_outage_list)):
        for j in range(0, len(stage_vector)):
            dynamic_temp_load_loss = dynamic_outage_at_specific_stages.DSS_Python_Interface1(filepath, load_file_name, blackout_criterion, system_name, dynamic_initial_outage, dynamic_stage_outage_list[k], stage_vector[j]);
            if (dynamic_temp_load_loss > worst_case_max_load_loss):
                worst_case_max_load_loss = dynamic_temp_load_loss;
                worst_case_dynamic_stage_outage = dynamic_stage_outage_list[k];
                temp_worst_case_stage_number = stage_vector[j];
#        dynamic_new_outage_list = maptest_updated_outage_list.maptest14bus_test_system(dynamic_stage_outage_list, worst_case_dynamic_stage_outage);
    print '############################################################################################'
    print 'Static Worst Case Attack: %s' %static_worst_case_outage
#    print 'Static Worst Case Load Loss: %s' %static_worst_case_load_loss
    print 'Dynamic Worst Case Initail Attack: %s' %dynamic_initial_outage_temp
    print 'Dynamic Worst Case "STAGE {0}" Attack: {1}'.format(temp_worst_case_stage_number,worst_case_dynamic_stage_outage)
    print "Dynamic Worst Case Load Loss: %s" %worst_case_max_load_loss
    print '############################################################################################'

    
worst_case_dynamic_attack("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2);
