import subprocess
import os
import re
import json

def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


json_path = "/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-binaries.json"
data = load_data(json_path)


given_type = "O3" 
given_id = 120

for item in data:
    if item["task_id"] == given_id and item["type"] == given_type:
        print(item["binary"])


