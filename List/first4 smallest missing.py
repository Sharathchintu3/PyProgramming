l = list(map(int, input().split()))
a = []
m = l[0]
for i in l:
    if i<m:
        m = i
c = 0
while c<4:
    if m not in l:
        a.append(m)
        c+=1
    m+=1
print(a)