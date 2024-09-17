import os

def write_filenames_to_txt(folder_path, output_txt_file):
    with open(output_txt_file, 'w') as f:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                f.write(f"{file}\n")

def find_and_write_file(folder_path, target_file_name, output_file_path):

    for root, dirs, files in os.walk(folder_path):
        if target_file_name in files:
            file_path = os.path.join(root, target_file_name)

            with open(file_path, 'r') as file:
                file_contents = file.read()

            with open(output_file_path, 'w') as output_file:
                output_file.write(file_contents)
                
            print(f"Contents of '{target_file_name}' written to '{output_file_path}'.")
            return
    
    print(f"File '{target_file_name}' not found in the directory '{folder_path}'.")

# # Example usage
# folder_path = "/home/wtegge2/LLM4Decompile/AnghaBench/binaryFiles"  # Replace with the path to your folder
# output_txt_file = "/home/wtegge2/LLM4Decompile/AnghaBench/list_of_binaries.txt"  # Replace with the desired output txt file path
# write_filenames_to_txt(folder_path, output_txt_file)

folder_path = "/home/wtegge2/LLM4Decompile/AnghaBench/binaryFiles" 
# target_file_name = "test_extr_bigdict.c_main.c_O3.o.txt"  
target_file_name = "test_extr_avstring.c_av_append_path_component.c_O3.o.txt"  
output_file_path = "/home/wtegge2/LLM4Decompile/AnghaBench/binary_output2.txt"  
find_and_write_file(folder_path, target_file_name, output_file_path)