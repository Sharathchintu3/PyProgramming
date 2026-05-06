l = list(map(int, input().split()))
for i in range(len(l)):
    a = l[0:i+1]
    c = 0
    for j in range(len(a)):
        if l[i] == l[j]:
            c+=1
    print(l[i], c)


# or

for i in range(len(l)):
    d = 0
    for j in range(0, i+1):
        if l[i] == l[j]:
            d+=1
    print(l[i], d)