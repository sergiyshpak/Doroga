# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:30:22 2019

@author: g705586
"""

import datetime

def exists2000(dict):
    #for d in dict:
        
    return True

def getLess2000(nodesM):
    resultList=[]
    for item in nodesM:
        if nodesM[item]<2000:
            resultList.append(item)
    return resultList

def get2000Sosedi(mech1,nodesM1):
    resultList1=[]
    # regular gates
    for para in regularGate:
        if para[0]==mech1:
            if nodesM1[para[1]]==2000:
                resultList1.append(para[1])
    #jump gates
    
    return resultList1


print(str(datetime.datetime.now()))

regularGate=[]
#    lines like  sysid,sysid     ex  30000777,30000778
# no headers
with open("RegularGates.csv", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        regularGate.append(my_list)


jumpGate=[]
#    lines like  sysid,sysid     ex  30000777,30000778
# no headers
with open("JumpGates.csv", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        jumpGate.append(my_list)




systemDictIdName= {} 
systemDictNameId={}
systemSec= {} 
#    lines like  reg_id, const_id, sys_id, sys_name, sec, fation_id
#  for ex 10000001,20000001,30000007,Yuzier,0.906555511,500007
# no headers
with open("SolarSystems.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDictIdName[my_list[2].strip()] = my_list[3].upper().strip()    #map id:name
        systemDictNameId[ my_list[3].upper().strip() ] =my_list[2].strip()    #map name:id
        systemSec[my_list[2].strip()] = my_list[4]     #map id:sec


#print(len(regularGate))

startSysa="Jita"
finishSysa="1DQ1-A"

startSysa=startSysa.upper()
finishSysa=finishSysa.upper()

print("Shortest Path from "+startSysa+" to "+finishSysa)

startSysaId=systemDictNameId.get(startSysa,"NONE")
finishSysaId=systemDictNameId.get(finishSysa,"NONE")

if startSysaId=="NONE" or finishSysaId=="NONE":
    print("Shortest Path from "+startSysaId+" to "+finishSysaId)
    exit
    
    
nodesMarked={}    

for noda in systemDictIdName:
    nodesMarked[noda]=2000
nodesMarked[startSysaId]=0
    
while nodesMarked.get(finishSysaId)==2000 and exists2000(nodesMarked):
    less2000=[]
    less2000=getLess2000(nodesMarked)
    #print("----------------")
    for mecheno in less2000:
     #   print("polo1 "+systemDictIdName.get(mecheno)+"  metka "+str(nodesMarked.get(mecheno)))
        currentNum=nodesMarked.get(mecheno)
        sosedi=[]
        sosedi=get2000Sosedi(mecheno,nodesMarked)
        for sosa in sosedi:
            nodesMarked[sosa]=currentNum+1
            
     
    
print ( "path length is "+str(nodesMarked.get(finishSysaId)))
print(str(datetime.datetime.now()))