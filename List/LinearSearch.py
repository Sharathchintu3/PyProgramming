l = list(map(int, input().split()))
key = int(input())
for i in range(0, len(l)):
    if l[i] == key:
        print("Found")
        break
else:
    print("Not Found")