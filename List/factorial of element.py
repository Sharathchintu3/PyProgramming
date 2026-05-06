l = list(map(int, input().split()))
a = []
for i in l:
    fact = 1
    for j in range(1, i+1):
        fact*=j
    a.append(fact)
    print(fact)
print(a)