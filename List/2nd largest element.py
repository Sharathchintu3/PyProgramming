l = list(map(int, input().split()))
max1 = max2 = -(10**6)
for i in range(0, len(l)):
    if l[i]>max1:
        max2 = max1
        max1 = l[i]
    elif l[i]>max2 and max1!=max2:
        max2 = l[i]
print(max2)