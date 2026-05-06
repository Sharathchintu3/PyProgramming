def p(a):
    if n<2:
        return False
    for i in range(2, int(n**0.5)):
        if n%i==0:
            return False
    return True

n = int(input())
l = [0]*(n(n+1))//2
for i in l:
    if p(n):
        i = n
print(l)