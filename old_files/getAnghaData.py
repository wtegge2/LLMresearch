import os
import json

def json_dump(json_file_path, data):
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def get_subdirectories_and_c_files(parent_directory):
    result = []

    # Loop through each item in the parent directory
    for item in os.listdir(parent_directory):
        item_path = os.path.join(parent_directory, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Check for .c files in the subdirectory
            c_files = [f for f in os.listdir(item_path) if f.endswith('.c')]
            
            # If no .c files, add entry with file_name as None
            if not c_files:
                result.append({"dir_name": item, "filename": None})
            else:
                # Add an entry for each .c file
                for c_file in c_files:
                    result.append({"dir_name": item, "filename": c_file})

    return result


def get_subdirectories_and_c_files_nested(parent_directory):
    result = []
    stack = [(parent_directory, None, None)]
    OPT = ["O0", "O1", "O2", "O3"]

    while stack:
        current_path, directory_name, subdirectory_name = stack.pop()

        # Loop through each item in the current directory
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            # Check if the item is a directory
            if os.path.isdir(item_path):
                # If we're at the first level, set directory_name
                if directory_name is None:
                    current_directory = item
                else:
                    current_directory = directory_name

                # For subdirectories, update subdirectory_name
                current_subdirectory = item if directory_name is not None else None

                # Add subdirectory to stack for further processing
                stack.append((item_path, current_directory, current_subdirectory))
            elif item.endswith('.c'):
                for opt_state in OPT:
                    # Add .c file entry
                    result.append({
                        "directory": directory_name,
                        "subdirectory": subdirectory_name,
                        "type": opt_state,
                        "filename": item,
                        "path": os.path.abspath(item_path)
                    })

    return result

def concat_lines(file_path):
    concatenated_string = ""
    with open(file_path, "r", encoding='utf-8') as file:
        lines = file.readlines()
        concatenated_string = ''.join(lines)  # Join lines as they are, preserving newlines
    return concatenated_string 
    

def get_c_code(dict, json_file_path):
    for item in dict:
        if item["directory"] == None or item["filename"] == None:
            item["c_func"] = None
            continue

        dir_path = item["path"]

        lines = concat_lines(dir_path)

        item["c_func"] = lines

    json_dump(json_file_path, dict)



directory_path = "/home/wtegge2/LLM4Decompile/AnghaBench/AnghaBench"

json_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data.json"

Angha_dict = get_subdirectories_and_c_files_nested(directory_path)

get_c_code(Angha_dict, json_path)



