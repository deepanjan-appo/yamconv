"""
This file is responsible for creating the list of tiers from the data variable.
"""
# pylint: disable=C
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
                temptier['containers'][j]['triggers'] = temptier['containers'][j]['lifecycle']
                del temptier['containers'][j]
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

    return tierlist
