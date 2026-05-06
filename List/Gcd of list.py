l = list(map(int, input().split()))
m = min(l)
while True:
    for i in range(0, len(l)):
        if not l[i]%m==0:
            m-=1
            break
    else:
        print(m)
        break
