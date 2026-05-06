l = list(map(int, input().split()))
mul = max(l)
m = mul
while True:
    for i in range(0, len(l)-1):
        if not mul%l[i]==0:
            mul+=m
            break
    else:
        print(mul)
        break