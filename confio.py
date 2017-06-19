import yaml, json

def json_loader(filepath):
    """Loads a Yaml file based on directory"""
    with open(filepath, "r") as file_descriptor:
        data = json.load(file_descriptor)
    return data
def yaml_dumper(filepath, data):
    """Dumps data to a YAML file"""
    with open(filepath, "w") as file_descriptor:
        yaml.safe_dump(data, file_descriptor, default_flow_style=False)

def yaml_loader(filepath):
    """Loads a Yaml file based on directory"""
    with open(filepath, "r") as file_descriptor:
        data = list(yaml.safe_load_all(file_descriptor))
    return data
