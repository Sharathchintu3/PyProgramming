a = input()
b = int(input())
num = 1
ch = ord(a)
for i in range(2, b+1):
    c =0
    for j in range(1, b-i+1):
        print(" ", end = "")
    for j in range(0, i):
        if c%2==0:
            print(num, end = " ")
            num+=b
        else:
            print( chr(ch), end = " ")
            ch+=1
        c+=1
    print()