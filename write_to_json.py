import json
def write_json(file, *args):
    paths = {}
    if len(args) == 4:
        paths["output_path"] = args[0]
        paths["input_file_path"] = args[1]
        paths["username"] = args[3]
    if len(args) == 2:
        paths["playlist"] = args[0]
        paths["songs"] = args[1]
    file_json = open(file, 'w')
    json.dump(paths, file_json)
