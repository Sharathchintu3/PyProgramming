l = list(map(int, input().split()))
for i in range(0, len(l)-1):
    if l[0]<l[1]:
        if l[i]>l[i+1]:
            print("Unsorted")
            break
    else:
        if l[i]<l[i+1]:
            print("Unsorted")
            break
else:
    if l[0]<l[1]:
        print("Asc Sort")
    else:
        print("Dsc Sort")