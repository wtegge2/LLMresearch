import subprocess
import os
import re
import json


def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data



def compile_c_code(data, fileName):

    count = 0
    for item in data: 

        with open(fileName+'.c', 'w') as f:
            print(item["c_func"] + " ", file=f)
            f.close()

        opt_state = str(item["type"])

        output_file = fileName + item["filename"]  + '_' + opt_state
        input_file = fileName+'.c'
        compile_command = f'gcc -c -o {output_file}.o {input_file} -{opt_state} -lm'#compile the code with GCC on Linux
        
        try: 
            subprocess.run(compile_command, shell=True, check=True)
            count = count + 1
        except subprocess.CalledProcessError as e:
            with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files3.txt", 'a') as fl:
                print(item["filename"] + " " + item["type"] + "\n", file=fl)
                fl.close()
            continue
        except Exception as e:
            with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files3.txt", 'a') as fl:
                print(item["filename"] + " " + item["type"] + "\n", file=fl)
                fl.close()
            continue

    print(count)


json_file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data-final.json"
data = load_data(json_file_path)

filename = '/home/wtegge2/LLM4Decompile/AnghaBench/copy/'

# for item in data:
#     print(item.keys())
#     print(item)
#     break

compile_c_code(data, filename)