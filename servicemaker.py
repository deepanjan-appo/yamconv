# pylint: disable=C
"""
This file is responsible for creating the list of services from the data variable.
"""
import templates
from copy import deepcopy

def getServiceNumber(data):
    serv_count = 0
    for i in data:
        if i['kind'] == 'Service' and 'spec' in i and 'selector' not in i['spec']:
            serv_count += 1
    return serv_count


def serviceListBuilder(data):
    servicelist = []
    bring = []
    for i in data:
        if i['kind'] == 'Service' and 'spec' in i and 'selector' not in i['spec']:
            bring.append(i)
    if len(bring) > 0:
        for j in data:
            for m in range(len(bring)):
                if j['kind'] == 'Endpoints' and j['metadata']['name'] == bring[m]['metadata']['name']:
                    bring[m]['subsets'] = deepcopy(j['subsets'])
        for p in bring:
            tempserv = deepcopy(templates.service_template)
            if 'name' in p['metadata']:
                tempserv['name'] = p['metadata']['name']
            if 'subsets' in p:
                tempserv['endpoints'] = deepcopy(p['subsets'])
                portcount = 0
                for i in range(len(tempserv['endpoints'])):
                    for j in range(len(tempserv['endpoints'][i]['ports'])):
                        tempserv['endpoints'][i]['ports'][j]['targetPort'] = p['spec']['ports'][portcount]['targetPort']
                        tempserv['endpoints'][i]['ports'][j]['protocol'] = p['spec']['ports'][portcount]['protocol']
                        portcount = (portcount+1)%(len(p['spec']['ports']))
            servicelist.append(tempserv)
    return servicelist
