import json
import os
def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))
    os.chdir(r"G:\abdallah\web\web_project_repo\json_data\all_data")
    with open('all_data.json', 'w') as output_file:
        json.dump(result, output_file)

os.chdir(r"G:\abdallah\web\web_project_repo\json_data")
json_files = [f for f in os.listdir() if f.endswith('.json')]
merge_JsonFiles(json_files)
print("Merged Successfully !")