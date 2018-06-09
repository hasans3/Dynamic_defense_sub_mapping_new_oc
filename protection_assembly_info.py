# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:52:18 2017

@author: saqibhasan

This is a supporting function for getting the appropriate protection assembly connected to the appropriate transmission lines.
It is used in greedy_algorithm_v2.py

"""

def protection_assembly_info(PA_file_name, wrst_case_outage):
    transmission_line_PA_names = [];
#    pr_assembly_dict = {'Line.tl12': ('PA_10','PA_9'),'Line.tl1011': ('PA_22','PA_21'),'Line.tl1213': ('PA_29','PA_30'),
#    'Line.tl25': ('PA_7','PA_8'),'Line.tl34': ('PA_3','PA_4'),'Line.tl24': ('PA_5','PA_6'),'Line.tl15': ('PA_11','PA_12'),
#    'Line.tl914': ('PA_34','PA_33'),'Line.tl612': ('PA_27','PA_28'),'Line.tl23': ('PA_1','PA_2'),'Line.tl1314': ('PA_31','PA_32'),
#    'Line.tl910': ('PA_20','PA_19'),'Line.tl611': ('PA_24','PA_23'),'Line.tl79': ('PA_17','PA_18'),'Line.tl78': ('PA_15','PA_16'),
#    'Line.tl45': ('PA_14','PA_13'),'Line.tl613': ('PA_25','PA_26')}
    file_data = open(PA_file_name, 'r')
    data = file_data.readline();
    pr_assembly_dict = eval(data);
    file_data.close()
#    wrst_case_outage = [['Line.tl34', 'Line.tl1011', 'Line.tl1213']]
#    print pr_assembly_dict['Line.tl1011']
    worst_case_outage_temp = wrst_case_outage;
    for i in range(0,len(worst_case_outage_temp)):
        wrst_case_outage_temp = worst_case_outage_temp[i];
        for j in range(0, len(wrst_case_outage_temp)):
            transmission_line_PA_names.append(pr_assembly_dict[wrst_case_outage_temp[j]])
#    print transmission_line_PA_names
    return transmission_line_PA_names

    
#protection_assembly_info("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\\transmissionlines_PA_names.txt", [[]]);