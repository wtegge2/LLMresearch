import json

def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# tests if a c file exists in the dataset when given the name
def find_c_file(c_file_name, json_file_path):
    
    data = load_data(json_file_path)

    for item in data:
        if item["filename"] == c_file_name:
            return False
        else:
            return True

def print_c_file(c_file_name, json_file_path, output_file):

    data = load_data(json_file_path)

    for item in data:
        if item["filename"] == c_file_name:
            with open(output_file, 'w') as f:
                print(item["c_func"] + " ", file=f)
                f.close()
                break




json_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data.json"
file = "extr_configuration.c_config_load.c"
result = find_c_file(file, json_path) 
output_file = "/home/wtegge2/LLM4Decompile/AnghaBench/output.c"

if result == False:
    print("Not Found!")
else: 
    print("Found file: " + file + "\n")
    print_c_file(file, json_path, output_file)
    
