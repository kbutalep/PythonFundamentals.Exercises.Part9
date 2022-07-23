import os, json, pickle



def read_json(path):
    open_json = open(path)
    json_object = json.load(open_json)
    return json_object

def read_all_json_files(path):
    all_json = []
    for files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                result = read_json(os.path.join(path, file))
                all_json.append(result)
    return all_json



