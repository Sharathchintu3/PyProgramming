def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

l = list(map(int, input().split()))
a = 0
ore=[]
for i in range(len(l)):
    for j in range(i, len(l)):
        s = 0
        res = []
        for k in range(i, j+1):
            s+=l[k]
            res.append(l[k])
        if isprime(s):
            if len(res)>a:
                if len(res)>len(ore):
                    ore = res
print(ore)