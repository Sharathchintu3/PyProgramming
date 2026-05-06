def p(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

l = list(map(int, input().split()))
c, s = 0, 0
for i in l:
    if p(i):
        c+=1
        s+=i
print(s/c)