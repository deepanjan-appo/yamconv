# pylint: disable=C
"""
This file contains the function namedDataCreator
for dividing the massive data set variable according to namespaces
"""
from copy import deepcopy
def namedDataCreator(data):
    namespace_array = []
    namespace_set = []
    named_data = {}
    for i in range(len(data)):
        if 'namespace' in data[i]['metadata']:
            namespace_array.append(data[i]['metadata']['namespace'])
    # print namespace_array
    namespace_set = list(set(namespace_array))


    if namespace_set:
        print namespace_set
        print "=========================="
        for j in namespace_set:
            named_data[j] = []
            for i in range(len(data)):
                if data[i]['metadata']['namespace'] == j:
                    named_data[j].append(deepcopy(data[i]))
        print named_data
    else:
        appname = raw_input("Enter a name for your app:")
        named_data[appname] = []
        for i in range(len(data)):
            named_data[appname].append(deepcopy(data[i]))
    return named_data