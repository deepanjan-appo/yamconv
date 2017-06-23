"""
This is the entrypoint for the code.
You run the entire program using entrypoint.py
"""

# pylint: disable=C
from copy import deepcopy
import datadef
import templates
import nameddatadef
import outfiledef

templates.greeting()

data = deepcopy(datadef.dataCreator())
named_data = deepcopy(nameddatadef.namedDataCreator(data))
result = outfiledef.outFileMaker(named_data)
if result == 0:
    print "\nOperation successful\n"
else:
    print "\nThere were errors\n"
