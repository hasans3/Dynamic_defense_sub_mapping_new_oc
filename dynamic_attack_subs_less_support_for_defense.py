# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 14:57:19 2017

@author: saqibhasan

DYNAMIC ATTACK GREEDY HUERISTICS SUPPORT FUNCTION
This method uses new open command.
"""

def greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_name1, prot_substation1):
    import cascade_algorithm_support_defense_subsless
    import maptest_new_outage_list_support_defense
    import cascade_algorithm_reduced_outages
    import obtain_subs_support_defense
    import time
    tot_exe_time_start = time.time()
    temp_max_loadloss = 0;
    worst_case_outage = [];
    worst_case_subs = {};
    loadloss_gain = 0;
    max_load_loss_outage, max_loadloss = cascade_algorithm_support_defense_subsless.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, s_name1, prot_substation1);
#    print max_load_loss_outage
    temp_max_loadloss = max_loadloss;
    worst_case_outage = max_load_loss_outage;  
    for k in range(0, (p_budget-1)):
        new_outage_list = maptest_new_outage_list_support_defense.maptest14bus_test_system(comp_filename, start_range, contingency_range, max_load_loss_outage, s_name1, prot_substation1);
#        print new_outage_list
        max_load_loss_outage, max_loadloss = cascade_algorithm_reduced_outages.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, new_outage_list);
        if (max_loadloss > temp_max_loadloss):
            temp_max_loadloss = max_loadloss;
            worst_case_outage = max_load_loss_outage;
        if ((loadloss_gain - temp_max_loadloss) == 0):
            break;
        else:
            loadloss_gain = temp_max_loadloss;
    worst_case_subs = obtain_subs_support_defense.maptest14bus_test_system(comp_filename, start_range, contingency_range, worst_case_outage, s_name1, prot_substation1)
    tot_exe_time_end = time.time()
    tot_exe_time = (tot_exe_time_end - tot_exe_time_start)
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print 'Worst case outage: %s' %worst_case_outage
    print 'Worst case loadloss: %s' %temp_max_loadloss
    print 'Worst case substations to be attacked: %s' %worst_case_subs
    print 'Total execution time in seconds: %s' %tot_exe_time
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    return (worst_case_subs, worst_case_outage, temp_max_loadloss)
#greedy_hueristics("'G:\saqib\open DSS\opendss_matlab_interface\ieee9bus_system.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\component_data_heuristics.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\Load_data_with_reactive_load.txt", 0, 1, 40, 'wscc9bus_system_test_N-1.xml', 2);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 2);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1_testing1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data_testing2.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 6);    


# -------------------------------------------- 
# need to work on this file to send the substations to be removed in order to compute the worst case attack after protecting the subs.