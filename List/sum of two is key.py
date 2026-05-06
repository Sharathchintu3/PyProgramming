l = list(map(int, input().split()))
key = int(input())
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]+l[j]==key:
            print(l[i], l[j])




# or




for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j]==key:
            print(l[i], l[j])
