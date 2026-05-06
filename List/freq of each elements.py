l = list(map(int, input().split()))
key = 0
for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[j] == l[i]:
            c+=1
    print(l[i], c)


# with method

for i in range(len(l)):
    print(l[i], l.count(l[i]))

