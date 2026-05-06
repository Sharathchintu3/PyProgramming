l = list(map(int, input().split()))
mc = 0
ele = 0
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i] == l[j]:
            c+=1
        if c>mc:
            mc = c
            ele = l[i]
print(ele)