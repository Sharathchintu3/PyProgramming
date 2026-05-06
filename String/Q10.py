s = input()
if len(s)==10 and s.isalnum():
    if s[0:5].isalpha() and s[0:5].isupper() and s[5:9].isdigit() and s[9].isalpha() and s[9].isupper():
        print(s)
    else:
        print("Invalid Pan Card")
else:
    print("Invalid Pan Card")


