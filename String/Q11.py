gmail = input()
a = len(gmail)-len("@gmail.com")
if gmail[0:a].isalnum() and gmail.islower():
    if gmail.endswith("@gmail.com"):
        print(gmail)
    else:
        print("Invalid gmail")
else:
    print("Invalid gmail")