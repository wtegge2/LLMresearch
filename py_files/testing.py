import subprocess
import os
import re
import json


def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def process_file(file_path):
    output_lines = []
    with open(file_path, "r") as file:
        for line in file:
            matches = hex_pattern.findall(line)
            for match in matches:
                output_lines.append(match)
                if line.find(match) + len(match) + 2 < len(line) and line[line.find(match) + len(match) + 1] == ' ':
                    break  # break if more than one space after the match
    return '\n'.join(output_lines)


def concat_lines(file_path):
    concatenated_string = ""
    with open(file_path, "r") as file:
        for line in file:
            concatenated_string += line.strip() + "\n" 
    return concatenated_string


######################################################################################################
# code to compile all given c code, run objdump to obtain binary and asm, and then store in txt file
######################################################################################################
json_file_path = "/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval.json"
data = load_data(json_file_path)

digit_pattern = r'\b0x[a-fA-F0-9]+\b'# binary codes in Hexadecimal
zeros_pattern = r'^0+\s'#0s
OPT = ["O0", "O1", "O2", "O3"]

fileName = '/home/wtegge2/LLM4Decompile/test/test'

for item in data: 
    with open('/home/wtegge2/LLM4Decompile/test/test.c', 'w') as f:
        print(item["c_func"] + " ", file=f)
        f.close()
    
    opt_state = str(item["type"])
    task_id = str(item["task_id"])
    output_file = fileName +'_' + task_id + '_' + opt_state
    input_file = fileName+'.c'
    compile_command = f'gcc -c -o {output_file}.o {input_file} -{opt_state} -lm' # compile 
    subprocess.run(compile_command, shell=True, check=True)
    compile_command = f'objdump -d {output_file}.o > {output_file}.txt' # disassemble into assembly instructions
    subprocess.run(compile_command, shell=True, check=True)


######################################################################################################
# code to search through each objdump output, extract binary/hex values, and dump into new txt files
######################################################################################################
directory_path = "/home/wtegge2/LLM4Decompile/test"
output_directory_path = "/home/wtegge2/LLM4Decompile/hex_binary_files"
hex_pattern = re.compile(r'(?<=\s)([0-9a-f]{2}(?:\s[0-9a-f]{2})*)(?=\s)', re.IGNORECASE)
os.makedirs(output_directory_path, exist_ok=True)


for filename in os.listdir(directory_path):
    all_hex_sequences = ""
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)

        output = process_file(file_path)
        if output: 
                all_hex_sequences += output + '\n'

        output_file_path = os.path.join(output_directory_path, f"{filename}_output.txt")
        with open(output_file_path, "w") as output_file:
            output_file.write(all_hex_sequences)
            output_file.close()


######################################################################################################
# code to edit the dictionary with new binary data and dump into a given json file
######################################################################################################
json_file_path = "/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-binaries.json"

new_directory_path = "/home/wtegge2/LLM4Decompile/hex_binary_files"
for filename, item in zip(os.listdir(new_directory_path), data):
    
    input_path = os.path.join(new_directory_path, filename)

    full_entry = concat_lines(input_path)

    item["binary"] = full_entry

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)





