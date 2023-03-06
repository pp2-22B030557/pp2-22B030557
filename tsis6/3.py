def is_palindrome(s):
    s = s.replace(" ", "").lower()
    reversed_s = s[::-1]
    
    if s == reversed_s:
        return True
    else:
        return False

string = input("Enter a string: ")

if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")