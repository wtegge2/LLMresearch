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


def c_to_asm(data, fileName, json_path):

    digit_pattern = r'\b0x[a-fA-F0-9]+\b'# binary codes in Hexadecimal
    zeros_pattern = r'^0+\s'#0s
    OPT = ["O0", "O1", "O2", "O3"]
    data = data.sort()

    for idx, item in enumerate(data): 
        if idx >= 0:

            with open(fileName+'.c', 'w') as f:
                print(item["c_func"] + " ", file=f)
                f.close()

            opt_state = str(item["type"])

            output_file = fileName +'_' + item["filename"]  + '_' + opt_state
            input_file = fileName+'.c'
            compile_command = f'gcc -c -o {output_file}.o {input_file} -{opt_state} -lm'#compile the code with GCC on Linux
        
            try: 
                subprocess.run(compile_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files2.txt", 'a') as fl:
                    print(item["filename"] + " " + item["type"] + "\n", file=fl)
                    fl.close()
                continue
            except Exception as e:
                with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files2.txt", 'a') as fl:
                    print(item["filename"] + " " + item["type"] + "\n", file=fl)
                    fl.close()
                continue

            compile_command = f'objdump -d {output_file}.o > {output_file}.s'#disassemble the binary file into assembly instructions
        
            try:
                subprocess.run(compile_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files2.txt", 'a') as fl:
                    print(item["filename"] + " " + item["type"] + "\n", file=fl)
                    fl.close()
                continue
            except Exception as e:
                with open("/home/wtegge2/LLM4Decompile/AnghaBench/bad_files2.txt", 'a') as fl:
                    print(item["filename"] + " " + item["type"] + "\n", file=fl)
                    fl.close()
                continue

            filename = output_file + '.s'

            if filename.endswith('.s'):
                opt_state = item["type"]
                input_asm = ''
                file_path = filename
                with open(file_path) as f:#asm file
                    asm= f.read()
                asm = asm.split('Disassembly of section .text:')[-1].strip()
                for tmp in asm.split('\n'):
                    tmp_asm = tmp.split('\t')[-1]#remove the binary code
                    tmp_asm = tmp_asm.split('#')[0].strip()#remove the comments
                    input_asm+=tmp_asm+'\n'
                input_asm = re.sub(zeros_pattern, '', input_asm)
                before = f"# This is the assembly code with {opt_state} optimization:\n"#prompt
                after = "\n# What is the source code?\n"#prompt
                input_asm_prompt = before+input_asm.strip()+after
                #with open(filename +'_' + opt_state +'.asm','w',encoding='utf-8') as f:
                #    f.write(input_asm_prompt)

                item["input_asm_prompt"] = input_asm_prompt
    
    json_dump(json_path, dict)


def get_asm(dict, directory, json_path):

    digit_pattern = r'\b0x[a-fA-F0-9]+\b'# binary codes in Hexadecimal
    zeros_pattern = r'^0+\s'#0s
    OPT = ["O0", "O1", "O2", "O3"]

    for filename, item in zip(os.listdir(directory_), data):
            if filename.endswith('.s'):
                opt_state = item["type"]
                input_asm = ''
                file_path = os.path.join(directory_, filename)
                with open(file_path) as f:#asm file
                    asm= f.read()
                asm = asm.split('Disassembly of section .text:')[-1].strip()
                for tmp in asm.split('\n'):
                    tmp_asm = tmp.split('\t')[-1]#remove the binary code
                    tmp_asm = tmp_asm.split('#')[0].strip()#remove the comments
                    input_asm+=tmp_asm+'\n'
                input_asm = re.sub(zeros_pattern, '', input_asm)
                before = f"# This is the assembly code with {opt_state} optimization:\n"#prompt
                after = "\n# What is the source code?\n"#prompt
                input_asm_prompt = before+input_asm.strip()+after
                #with open(filename +'_' + opt_state +'.asm','w',encoding='utf-8') as f:
                #    f.write(input_asm_prompt)
                
                item["input_asm_prompt"] = input_asm_prompt
    
    json_dump(json_path, dict)

def delete_non_s_files(directory):
    # Loop through each item in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if the item is a file and does not end with .s
        if os.path.isfile(file_path) and not filename.endswith('.s'):
            # Delete the file
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

                
json_file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/angha-data.json"
data = load_data(json_file_path)

filename = '/home/wtegge2/LLM4Decompile/AnghaBench/test/test'

json_ = '/home/wtegge2/LLM4Decompile/AnghaBench/angha-data-asm.json'

c_to_asm(data, filename, json_)

# directory_ = '/home/wtegge2/LLM4Decompile/AnghaBench/test'

# delete_non_s_files(directory_)

# get_asm(data, directory_, json_)

