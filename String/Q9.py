# s = input()
# if len(s)==12 and s.isdigit():
#     if s.startswith("0") or s.startswith("1"):
#         print("Invalid Aadhar Number")
#     else:
#         print(s)
# else:
#     print("Invalid Aadhar Number")
#


aad = input()
l = len(aad)
if l==12:
    c = 0
    for i in aad:
        a = ord(i)
        if a>=48 and a<=57:
            c+=1
        else:
            print("Invalid Aadhar")
            break
    if c==12:
        print("Valid Aadhar")
elif l==14:
    c = 0
    for i in range(l):
        a = ord(aad[i])
        if i==4 or i==9 and aad[i]==" ":
            c+=1
        elif i != 4 and i != 9 and a>=48 and a<=57:
            c+=1
        else:
            print("Invalid Aadhar")
            break
    if c==14:
        print("Valid Aadhar")
else:
    print("Invalid Aadhar")