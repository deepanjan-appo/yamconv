# pylint: disable=C
"""
This python file contains the outFileMaker function which is responsible for
creating the output data structure
and writing it to a file
"""
from copy import deepcopy
from sys import platform
import os
import templates
import tiermaker
import servicemaker
import confio

def outFileMaker(named_data):
    for key in named_data:
        outfile = deepcopy(templates.file_template)
        app_name = key
        outfile['app_id'] = app_name
        outfile['tiers'] = deepcopy(tiermaker.tierListBuilder(named_data[key]))
        if servicemaker.getServiceNumber(named_data[key]) > 0:
            outfile['services'] = deepcopy(servicemaker.serviceListBuilder(named_data[key]))

        if platform == "win32":
            #filepath_write = raw_input("\n Enter a file with its path to write to e.g. C:\Users\Admin\Desktop\output.yaml : ")
            #filepath_write = "D:\\output_files\\" + key + ".yaml"
            filepath_write = os.path.expanduser("~\\Documents\\"+key+".yaml")
        #elif platform == "linux" or platform == "linux2" or platform == "darwin":
        else:
            directory = os.path.expanduser("~/appOrbitTemplate")
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath_write = os.path.expanduser("~/appOrbitTemplate/"+key+".yaml")
        

        print "\nOutput file generated at " + filepath_write
        confio.yaml_dumper(filepath_write, outfile)
    return 0
