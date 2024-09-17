import subprocess
import os
import re
import json


def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def json_dump(json_file_path, data):
    with open(json_file_path, 'w') as json_file:     # change to append 'a'
        json.dump(data, json_file, indent=4)

def remove_indices_from_list(dict_list, index_file_path):
    # Read the indices from the file
    with open(index_file_path, "r") as file:
        indices = file.readlines()
    
    # Convert indices to integers and sort in descending order
    indices = sorted([int(index.strip()) for index in indices], reverse=True)
    
    # Remove the entries at the specified indices
    for index in indices:
        if 0 <= index < len(dict_list):
            del dict_list[index]
        else:
            print(f"Index {index} out of range. Skipping.")
    
    return dict_list


json_file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data-asm.json"
data = load_data(json_file_path)

filename = '/home/wtegge2/LLM4Decompile/AnghaBench/missing_key_indices.txt'

json_ = '/home/wtegge2/LLM4Decompile/AnghaBench/angha-data-final.json'

result = remove_indices_from_list(data, filename)

json_dump(json_, result)

