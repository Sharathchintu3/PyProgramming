l = list(map(int, input().split()))
key = int(input())
for i in range(len(l)):
    for j in range(i, len(l)):
        a = 0
        res = []
        for k in range(i, j+1):
            res.append(l[k])
            a += l[k]
        if a == key:
            print(res)