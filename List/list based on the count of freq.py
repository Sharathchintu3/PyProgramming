l = list(map(int, input().split()))
f = [0]*len(l)
for i in range(len(l)):
    oc = l.count(l[i])
    f[i] = oc
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if f[i]<f[j]:
            f[i], f[j] = f[j], f[i]
            l[i], l[j] = l[j], l[i]

for i in range(len(l)):
    bc = 0
    for j in range(0, i+1):
        if l[i]==l[j]:
          bc+=1
    if bc == 1:
        print(l[i], f[i])