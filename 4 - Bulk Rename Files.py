
# Import required libraries
import os

# Get desired inputs from user
folder_path = input("Enter the folder path: ")
name_prefix = input("Enter the name prefix: ")

all_files = os.listdir(folder_path)
print("Old Filenames:", all_files)

ignore_files = [".git"]

count = 1
for file in all_files:
    if file not in ignore_files:
        file_extension = os.path.splitext(file)[1]
        new_name = name_prefix + str(count) + file_extension
        os.rename(folder_path + "/" + file, folder_path + "/" + new_name)
        count += 1

all_files = os.listdir(folder_path)
print("New Filenames:", all_files)
