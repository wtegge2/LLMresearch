import os
import shutil

def move_o_files(source_folder, destination_folder):
    # Create destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)
    count = 0

    # Loop through each item in the source folder
    for item in os.listdir(source_folder):
        # Check if the item is a .o file
        if item.endswith('.o'):
            # Construct the full file paths
            source_file_path = os.path.join(source_folder, item)
            destination_file_path = os.path.join(destination_folder, item)
            
            # Move the file
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} to {destination_file_path}")
            count = count + 1
    
    return count

# Example usage
source_folder = "/home/wtegge2/LLM4Decompile/AnghaBench/test"  # Replace with the path to your source folder
destination_folder = "/home/wtegge2/LLM4Decompile/AnghaBench/objectFiles"  # Replace with the path to your destination folder

total_object_files = 0
total_object_files = move_o_files(source_folder, destination_folder)
print(total_object_files)

