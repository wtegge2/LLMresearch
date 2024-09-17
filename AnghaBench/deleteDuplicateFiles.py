import os

def delete_duplicate_files(folder_path):
    # Create a set to keep track of seen file names
    seen_files = set()
    count = 0
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the current item is a file (not a directory)
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # If the file name has already been seen, delete the file
            if filename in seen_files:
                os.remove(file_path)
                print(f"Deleted duplicate file: {file_path}")
                count = count + 1
            else:
                # If not, add the file name to the set of seen files
                seen_files.add(filename)
    return count

# Example usage
folder_path = "/home/wtegge2/LLM4Decompile/AnghaBench/objectFiles"  # Replace with the path to your folder

number_of_duplicates_deleted = 0
number_of_duplicates_deleted = delete_duplicate_files(folder_path)
print(number_of_duplicates_deleted)