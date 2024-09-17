import os
import subprocess

def convert_o_files_to_hex_binary(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    count = 0
    
    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.o'):
            input_file_path = os.path.join(input_folder, filename)
            output_file_base = os.path.splitext(filename)[0]  # Remove the .o extension
            output_file_path = os.path.join(output_folder, filename + '.txt')
            
            # Run the `xxd -b` command and capture the output
            result = subprocess.run(['xxd', '-b', input_file_path], capture_output=True, text=True)
            
            # Write the output to the new .txt file
            with open(output_file_path, 'w') as output_file:
                output_file.write(result.stdout)
            
            print(f"Processed {filename}")

            count = count + 1
    
    return count


# Example usage
input_folder = "/home/wtegge2/LLM4Decompile/AnghaBench/objectFiles"  # Replace with the path to your folder with .o files
output_folder = "/home/wtegge2/LLM4Decompile/AnghaBench/binaryFiles"  # Replace with the path to your desired output folder

files_converted = 0
files_converted = convert_o_files_to_hex_binary(input_folder, output_folder)
print(files_converted)