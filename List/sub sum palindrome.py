def ispal(n):
    t = n
    rev = 0
    while n>0:
        r = n%10
        rev = rev*10+r
        n=n//10
    if t==rev:
        return True
    return False

l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(i, len(l)):
        s = 0
        res = []
        for k in range(i, j+1):
            s += l[k]
            res.append(l[k])
        if ispal(s):
            print(res)