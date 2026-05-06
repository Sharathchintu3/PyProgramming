l = list(map(int, input().split()))
l.sort()
s = 0
e = len(l)-1
key = int(input())
while s<=e:
    mid = (s+e)//2
    if key == l[mid]:
        print("Found")
        break
    elif l[mid]<key:
        s = mid+1
    else:
        e = mid-1
else:
    print("Not Found")