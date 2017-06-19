"""
This is the entrypoint for the code.
You run the entire program using entrypoint.py
"""

# pylint: disable=C
from copy import deepcopy
import confio
import datadef
import templates
import tiermaker
import servicemaker
templates.greeting()

data = deepcopy(datadef.dataCreator())

outfile = deepcopy(templates.file_template)
app_name = raw_input("Enter the name of your App: ")
outfile['app_id'] = app_name
outfile['tiers'] = deepcopy(tiermaker.tierListBuilder(data))
if servicemaker.getServiceNumber(data) > 0:
    outfile['services'] = deepcopy(servicemaker.serviceListBuilder(data))


#filepath_write = raw_input("\n Enter a file with its path to write to e.g. C:\Users\Admin\Desktop\output.yaml : ")
filepath_write = "D:\output.yaml"
print "\nOutput file generated at " + filepath_write
confio.yaml_dumper(filepath_write, outfile)
