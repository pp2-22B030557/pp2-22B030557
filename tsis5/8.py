import re

string = input("Enter a string: ")
split_string = re.findall('[A-Z][^A-Z]*', string)
print("Split string:", split_string)