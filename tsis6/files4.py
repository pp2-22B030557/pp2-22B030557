file_path = 'path/to/text/file.txt'

with open(file_path, 'r') as f:
    num_lines = sum(1 for line in f)
    
print("Number of lines:", num_lines)