l = list(map(int, input().split()))
s, e = 0, len(l)-1
while s<e:
    if l[s]%2==0 and l[e]%2==0:
        l[s], l[e] = l[e], l[s]
        s+=1
        e-=1
    elif l[s]%2==0:
        e-=1
    else:
        s+=1
print(l)