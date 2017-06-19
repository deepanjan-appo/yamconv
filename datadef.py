# pylint: disable=C
import os, glob

import confio


def dataCreator():
    while (1):
        lang = raw_input("Enter J for JSON template input or Y for YAML template input: ")
        if lang == "J" or lang == "j":
            while (1):
                filepath_read = raw_input("Enter a valid directory containing JSON files: ")
                if os.path.exists(filepath_read) == False:
                    print "ERROR: That is not a valid directory. Try again? : "
                elif not any(fname.endswith('.json') for fname in os.listdir(filepath_read)):
                    print "ERROR: Your directory does not seem to contain any JSON files. Try again? : "
                else:
                    break
            direc = filepath_read
            arr = []
            data = []
            os.chdir(direc)
            for file in glob.glob('*.json'):
                arr.append(confio.json_loader(file))
            for i in arr:
                data.append(i)
            for j in data:
                if 'kind' in j:
                    return data
                    break
            else:
                print "ERROR: There is no kind parameter in the JSON file(s). Doesn't seem to be a valid K8s template."
                continue
            break
        elif lang == "Y" or lang == "y":
            while (1):
                typechoice = raw_input(
                    "Enter 1 (for single all-in-one YAML 1.2 file) OR 2 (for many YAML 1.1- files in a directory): ")
                if typechoice == "1":
                    while (1):
                        filepath_read = raw_input("Enter a valid YAML 1.2 file as a path: ")
                        if ((os.path.exists(filepath_read) == True) and (
                                    filepath_read.lower().endswith('.yml') or filepath_read.lower().endswith('.yaml'))):
                            break
                        else:
                            print "ERROR: Enter a valid YAML file"
                    data = confio.yaml_loader(filepath_read)
                    return data
                    break
                elif typechoice == "2":
                    while (1):
                        filepath_read = raw_input("Enter a valid directory containing YAML files: ")
                        if (os.path.exists(filepath_read) == False):
                            print "ERROR: That is not a valid directory. Try again? : "
                        elif not any(fname.endswith(('.yaml', '.yml')) for fname in os.listdir(filepath_read)):
                            print "ERROR: Your directory does not seem to contain any yaml files. Try again? : "
                        else:
                            break
                    direc = filepath_read
                    arr = []
                    data = []
                    os.chdir(direc)
                    for file in glob.glob('*.y*ml'):
                        arr.append(confio.yaml_loader(file))
                    for i in arr:
                        data.append(i[0])
                    for j in data:
                        if 'kind' in j:
                            return data
                            break
                    else:
                        print "ERROR: There is no kind parameter in the yaml file(s). Doesn't seem to be a valid K8s template."
                        continue
                    break
                else:
                    print "ERROR: Either 1 or 2. Those are the options.\n"
                break
        else:
            print "ERROR: Choose a valid language please. "
