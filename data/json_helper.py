import os
import json
import pickle



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

def write_pickle(path):
    outfile = open('super_smash_characters.pickle', 'wb')
    pickle.dump(path, outfile)

write_pickle('/Users/Kendra/Python/PythonFundamentals.Exercises.Part9')

def load_pickle(path):
    load_file = open(path, 'rb')
    return pickle.load(load_file)

print(load_pickle('super_smash_characters.pickle'))
