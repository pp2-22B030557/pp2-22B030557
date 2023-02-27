import re

string = input("Enter a string: ")
pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, string)
if matches:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")