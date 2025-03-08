s = "one piece"
rev = ""
for i in  range(len(s)-1, -1, -1):
    rev = rev + s[i]
if s == rev:
    print("It is a palindrome") 
else:
    print("Not a palindrome")       