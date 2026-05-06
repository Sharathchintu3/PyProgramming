l = list(map(int, input().split()))
m = -(10**6)
for i in range(0, len(l)):
    if m<l[i]:
        m = l[i]
print(m)