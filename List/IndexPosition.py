l = list(map(int, input().split()))
key = int(input())
for i in range(0, len(l)):
    if key == l[i]:
        print(i)