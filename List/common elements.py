l = list(map(int, input().split()))
l1 = list(map(int, input().split()))

for i in range(len(l)):
    for j in range(len(l1)):
        if l[i] == l1[j]:
            if l[i] in l:
                print(l[i])
                l.remove(l[i])
            elif l1[j] in l1:
                print(l1[j])
                l1.remove(l[j])



# 1 1 2 3 1 4 1 5
# 1 2 5 1 3 7 9 9