import json
import os
import subprocess
import re

def merge_binary_lines(input_file):
    with open(input_file, 'rb') as f_in:
        content = f_in.read()
    with open(input_file, 'w') as f_in:
        f_in.truncate(0)

    merged_line = ''.join(chr(byte) for byte in content)
    return merged_line


def load_data():
    with open('/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-test.json', 'r') as json_file:
        data = json.load(json_file)
    return data


def run_objdump_and_save_output(input_file, output_file):
    try:
        # Execute objdump command and capture the output
        result = subprocess.run(['objdump', '-d', input_file], stdout=subprocess.PIPE, check=True)
        # Write each line of the captured output to the specified file
        with open(output_file, 'w') as f:
            for line in result.stdout.decode().split('\n'):
                f.write(line + '\n')
        print("objdump command executed successfully. Output saved to", output_file)
    except subprocess.CalledProcessError as e:
        print("Error:", e)


data = load_data()
# with open('/home/wtegge2/LLM4Decompile/out.c', 'w') as f:
#     for item in data:
#         if(item["type"] == "O0"):
#             print(item["c_func"] + " ", file=f)
#             os.system("gcc -c -O0 out.c")
#             item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/out.o')
#             f.truncate(0) 
#         elif(item["type"] == "O1"):
#             print(item["c_func"] + " ", file=f)
#             os.system("gcc -c -O1 out.c")
#             item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/out.o')
#             f.truncate(0) 
#         elif(item["type"] == "O2"):
#             print(item["c_func"] + " ", file=f)
#             os.system("gcc -c -O2 out.c")
#             item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/out.o')
#             f.truncate(0) 
#         elif(item["type"] == "O3"):
#             print(item["c_func"] + " ", file=f)
#             os.system("gcc -c -O3 out.c")
#             item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/out.o')
#             f.truncate(0) 
with open('/home/wtegge2/LLM4Decompile/out.c', 'w') as f:
    for item in data:
        if(item["type"] == "O0"):
            print(item["c_func"] + " ", file=f)
            
            opt_state = "O0"
            output_file = '/home/wtegge2/LLM4Decompile/out'
            output = "/home/wtegge2/LLM4Decompile/objdump_output.out"
            compile_command = f'gcc -c -o {output_file}.o -{opt_state} -lm'#compile the code with GCC on Linux
            subprocess.run(compile_command, shell=True, check=True)
            
            compile_command = f'objdump -d {output_file}.o > {output}'#disassemble the binary file into assembly instructions
            subprocess.run(compile_command, shell=True, check=True)
            
            break

        elif(item["type"] == "O1"):
            print(item["c_func"] + " ", file=f)
            os.system("gcc -c -O1 out.c")
        elif(item["type"] == "O2"):
            print(item["c_func"] + " ", file=f)
            os.system("gcc -c -O2 out.c")
        elif(item["type"] == "O3"):
            print(item["c_func"] + " ", file=f)
            os.system("gcc -c -O3 out.c")

        item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/objdump_output.out')
        #if (i == 1):
        #    break
        #i = i + 1
        # f.read()
        f.seek(0)
        f.truncate(0)

    item["binary"] = merge_binary_lines('/home/wtegge2/LLM4Decompile/objdump_output.out')

with open('/home/wtegge2/LLM4Decompile/decompile-eval/decompile-eval-binaries.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)