# pylint: disable=C
"""
This file is responsible for creating the list of tiers from the data variable.
"""
import templates
from copy import deepcopy

def tierListBuilder(data):
    tierlist = []
    j = 0
    bring = []
    for i in data:
        if i['kind'] == 'Deployment' or i['kind'] == 'ReplicationController' or i['kind'] == 'Pod':
            bring.append(i)

    for p in bring:
        # print p['metadata']['name']
        temptier = deepcopy(templates.tier_template)
        if 'name' in p['metadata']:
            temptier['name'] = p['metadata']['name']
        if 'kind' in p:
            temptier['type'] = p['kind']
        if 'replicas' in p['spec']:
            temptier['replicas'] = p['spec']['replicas']
        temptier['containers'] = deepcopy(p['spec']['template']['spec']['containers'])
        # print temptier['containers'][0]
        for j in range(len(temptier['containers'])):
            if 'lifecycle' in temptier['containers'][j]:
                temptier['containers'][j]['triggers'] = deepcopy(temptier['containers'][j]['lifecycle'])
                del temptier['containers'][j]['lifecycle']
            if 'env' in temptier['containers'][j]:
                # print temptier['containers'][0]['env']
                for i in temptier['containers'][j]['env'][:]:
                    if 'valueFrom' in i:
                        temptier['containers'][j]['env'].remove(i)
            if 'volumeMounts' in p['spec']['template']['spec']['containers'][j]:
                del temptier['containers'][j]['volumeMounts']
                volumecount = len(p['spec']['template']['spec']['containers'][j]['volumeMounts'])
                volumelist = []
                for vol in range(volumecount):
                    tempvol = deepcopy(templates.volume_template)
                    tempvol['containerVolume'] = str(p['spec']['template']['spec']['containers'][j]['volumeMounts'][vol]['mountPath'])
                    # print p['spec']['template']['spec']['volumes'][vol]['persistentVolumeClaim']['claimName']
                    for x in data:
                        # print x['metadata']['name']
                        # print x['kind']
                        if x['kind'] == "PersistentVolumeClaim" and x['metadata']['name'] == p['spec']['template']['spec']['volumes'][vol]['persistentVolumeClaim']['claimName']:
                            gibgb = x['spec']['resources']['requests']['storage']
                            if gibgb.endswith("iB") or gibgb.endswith("ib"):
                                sizer = str(int(gibgb[:-3])*1.074)+gibgb[-3]
                                # print sizer
                                tempvol['min-size'] = sizer
                            elif gibgb.endswith("i") or gibgb.endswith("I"):
                                sizer = str(int(gibgb[:-2]) * 1.074) + gibgb[-2]
                                # print sizer
                                tempvol['min-size'] = sizer
                            elif gibgb.endswith("B") or gibgb.endswith("b"):
                                sizer = gibgb[:-1]
                                tempvol['min-size'] = sizer
                            else:
                                tempvol['min-size'] = x['spec']['resources']['requests']['storage']
                    volumelist.append(tempvol)
                temptier['containers'][j]['volumes'] = volumelist
        # print temptier['containers'][j]
        # print volumelist

        
        tierlist.append(temptier)
    print "Tiers detected are: "
    i = 1
    for tr in tierlist:
        print i , " : " , tr['name']
        i += 1
    orderchoice = raw_input("Do you wish to change ordering? Y/N")
    if orderchoice == "Y" or orderchoice == "y":
        #print "Enter the order as comma separated values without space e.g. 1,2,3 :"
        userlistorder = raw_input("Enter the order as comma separated values without space e.g. 3,1,2 :")
        myorder = [int(x) for x in userlistorder.split(",")]
        orderedlist = []

        #for j in range(len(userlistorder)):
        #    orderedlist.append(tierlist[ord(userlistorder[j])-1])
        orderedlist = [ tierlist[i-1] for i in myorder]
        
        return orderedlist

    return tierlist
