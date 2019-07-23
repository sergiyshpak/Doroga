# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:30:22 2019

@author: g705586
"""



import requests
import json
import time 
import sys
import math


regularGate={}
#    lines like  sysid,sysid     ex  30000777,30000778
# no headers
with open("RegularGates.csv", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        regularGate[my_list[0]] = my_list[1]

systemDict= {} 
systemSec= {} 
#    lines like  reg_id, const_id, sys_id, sys_name, sec, fation_id
#  for ex 10000001,20000001,30000007,Yuzier,0.906555511,500007
# no headers
with open("SolarSystems.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3].upper()    #map id:name
        systemSec[my_list[2]] = my_list[4]     #map id:sec


startSysa="Jita"
finishSysa="1DQ1-A"


startSysa=startSysa.upper()
finishSysa=finishSysa.upper()