my_list = [1, 2, 3, 4, 5]
file_path = 'path/to/new/file.txt'

with open(file_path, 'w') as f:
    for item in my_list:
        f.write("%s\n" % item)