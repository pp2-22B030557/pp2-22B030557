import string

for letter in string.ascii_uppercase:
    file_path = f"{letter}.txt"
    with open(file_path, 'w') as f:
        f.write(f"This is file {letter}.txt\n")