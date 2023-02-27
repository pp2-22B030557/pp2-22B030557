import re

string = input("Enter a string: ")
new_string = re.sub(r'(?<!\ )[A-Z]', ' \\g<0>', string).strip()
print("New string:", new_string)