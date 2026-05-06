def p(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

l = list(map(int, input().split()))
for i in l:
    nxt = i+1
    while True:
        if p(nxt):
            print(nxt)
            break
        nxt+=1