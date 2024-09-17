import json

def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

json_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data.json"

data = load_data(json_path)

for item in data:
    if item["type"] == "O0" and item["filename"] == "extr_ifxmips_atm_amazon_se.c_ase_fw_ver.c" and item["subdirectory"] == "src" and item["directory"] == "lede":
        file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/file_test.c"
        with open(file_path, 'w') as file_:
            print(item["c_func"], file=file_)
        break


        
