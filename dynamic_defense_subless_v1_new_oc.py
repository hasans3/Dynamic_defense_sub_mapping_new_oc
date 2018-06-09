# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:50:21 2018

@author: saqibhasan

This method provides the defense startegy for the dynamic attack scenario where it maps the substations back to the respective protection assemblies
that are associated with the respective transmission line in the system.
This method uses new open command.
"""
def dynamic_defense_subs_less(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, d_budget):

    import time
    import dynamic_defense_subsless_v1_support
    import support_for_dynamic_defense_subsless_v1
    import support_for_dynamic_defense_subsless_v2
    import dynamic_attack_subs_less_support_for_defense
    import cascade_algorithm_support_defense_subsless
    import maptest_new_outage_list_support_defense
    import obtain_subs_support_defense
    import maptest_testing_trimmed_defense
    import dynamic_attack_subs_less_support_for_defense_v2
    import cascade_algorithm_support_defense_subsless_v2
    import maptest_new_outage_list_support_defense_v2
    import obtain_subs_support_defense_v2
    import maptest_testing_trimmed_defense_v2
    import post_defense_dynamic_attack_subsless_support_v1
    
    tot_exe_time_start = time.time()
    temp_sub_protected = [];
    sub_protected = [];
    sub_protected1 = [];
    temp_worst_case_dict = {};
    prev_post_defese_loadloss_arr = [];
    temp_max_loadloss = 100;
    prev_post_defese_loadloss = 100;
    temp_worst_case_loadloss, temp_worst_case_outage, temp_worst_case_sub_dict, temp_worst_case_outage_vec = dynamic_defense_subsless_v1_support.worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget);
#    print temp_worst_case_loadloss, temp_worst_case_outage, temp_worst_case_sub_dict, temp_worst_case_outage_vec
    prev_post_defese_loadloss_arr.append(prev_post_defese_loadloss)
    pre_defense_worst_case_outage = temp_worst_case_outage;
    pre_defense_worst_case_loadloss = temp_worst_case_loadloss;
    pre_defense_worst_case_subs = temp_worst_case_sub_dict.values();
    temp_worst_case_sub = temp_worst_case_sub_dict.values();
    temp_worst_case_dict = temp_worst_case_sub_dict
#    print pre_defense_worst_case_subs
    for i in range(0, d_budget):
        temp_max_loadloss = 100;
        flag = 0;
        temp_worst_case_sub1 = [];
        if (len(sub_protected) != 0):
            prev_post_defese_loadloss, b, temp_worst_case_sub_dict = support_for_dynamic_defense_subsless_v2.worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, sub_protected);
            prev_post_defese_loadloss_arr.append(prev_post_defese_loadloss)            
            for keys in temp_worst_case_sub_dict:
                temp_worst_case_sub1.append(temp_worst_case_sub_dict[keys])             
            temp_worst_case_sub = temp_worst_case_sub1;
        for item in range(0, len(temp_worst_case_sub)):
            temp_worst_case_loadloss, temp_worst_case_outage, temp_worst_case_substation_dict = support_for_dynamic_defense_subsless_v1.worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, tuple([temp_worst_case_sub[item]]), sub_protected);
            if (temp_worst_case_loadloss < temp_max_loadloss):
                temp_max_loadloss = temp_worst_case_loadloss
                temp_sub_protected = temp_worst_case_sub[item];
                flag = 1;
        sub_protected.append(temp_sub_protected);
#        print sub_protected
        sub_protected1.append(temp_sub_protected);
        if (temp_max_loadloss > min(prev_post_defese_loadloss_arr) and flag == 1):
            sub_protected1.remove(temp_sub_protected);
        else:
            sub_protected1 = []
            for item in sub_protected:
                sub_protected1.append(item)
    post_defense_worst_case_loadloss, post_defense_worst_case_outage, post_defense_worst_case_outage_vec, post_defense_worst_case_sub_dict = post_defense_dynamic_attack_subsless_support_v1.worst_case_dynamic_attack(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, sub_protected1);
#    print post_defense_worst_case_loadloss, post_defense_worst_case_outage, post_defense_worst_case_outage_vec, post_defense_worst_case_dict
#    print pre_defense_worst_case_loadloss, sub_protected
    tot_exe_time_end = time.time()
    tot_exe_time = (tot_exe_time_end - tot_exe_time_start) 
    print '**************************************************************************************************************************'
    print 'Pre defense worst case dynamic-attack outages: %s' %pre_defense_worst_case_outage
    print 'Pre defense worst case dynamic-attack on substations: {0}'.format(pre_defense_worst_case_subs)
    print 'Pre defense worst case dynamic-attack load loss: %f' %pre_defense_worst_case_loadloss
    print 'Pre defense worst case dynamic-attack outage vector: %s' %temp_worst_case_outage_vec
    print 'Pre defense worst case dynamic-attack on substations sequence: %s' %temp_worst_case_dict
    print 'Substations to be proteceted: %s' %sub_protected1
    print 'Post defense worst case dynamic-attack outages: %s' %post_defense_worst_case_outage
    print 'Post defense worst case dynamic-attack on substations: {0}'.format(post_defense_worst_case_sub_dict.values())
    print 'Post defense worst case dynamic-attack load loss: %f' %post_defense_worst_case_loadloss
    print 'Post defense worst case dynamic-attack outage vectors: %s' %post_defense_worst_case_outage_vec
    print 'Post defense worst case dynamic-attack on substations sequence: %s' %post_defense_worst_case_sub_dict
    print 'Post defense percentage reduction in load loss: {0}%'.format(((pre_defense_worst_case_loadloss - post_defense_worst_case_loadloss)/pre_defense_worst_case_loadloss)*100)
    print 'Total execution time in seconds: %s' %tot_exe_time
    print '**************************************************************************************************************************'

#dynamic_defense_subs_less("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base_testing.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1_testing.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2, 14);
#dynamic_defense_subs_less("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing2.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2, 2);    

# ------------------------------------------- testing modified IEEE 57 bus system --------------------------------
dynamic_defense_subs_less("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1_new_oc_test.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing2_new_oc_test.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 3, 20);    

