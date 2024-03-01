import os
import re

folder_path = os.path.dirname(os.path.abspath(__file__))

# Function to get all file names in a folder
def list_files(folder_path):
    ignore_files = ["readme-generator.py", ".git", "README.md", ".DS_Store", ".gitignore" ]
    files = os.listdir(folder_path)
    # Filter out ignored files
    files = [file for file in files if file not in ignore_files]
    return files

# Function to format file names
def format_file_names(files):
    formatted_files = []
    for file in files:
        # Remove file extension
        file_name = os.path.splitext(file)[0]
        # Replace '-' with space and capitalize first letter
        formatted_name = file_name.replace("-", " ").capitalize()
        formatted_files.append(formatted_name)
    return formatted_files

# Function to write file names to README.md
def write_to_readme(files):
    with open("README.md", "w") as readme_file:
        readme_file.write("# Data Structures and Algorithms Solutions\n\n")
        for file in files:
            readme_file.write(f"- {file}\n")

# Function to sort formatted file names based on numerical count
def sort_file_names(files):
    sorted_files = sorted(files, key=lambda x: [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', x)])
    return sorted_files

# Get the list of files
files = list_files(folder_path)

# Format file names
formatted_files = format_file_names(files)

# Sort formatted file names word by word
sorted_files = sort_file_names(formatted_files)

# Write the sorted and formatted file names to README.md
write_to_readme(sorted_files)