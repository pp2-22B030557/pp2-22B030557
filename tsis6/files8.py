import os

file_path = 'path/to/file.txt'

if os.access(file_path, os.F_OK):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    else:
        print(f"You do not have permission to delete the file {file_path}.")
else:
    print(f"The file {file_path} does not exist.")