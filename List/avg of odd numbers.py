l = list(map(int, input().split()))
s = 0
c =0
for i in l:
    if i%2==1:
        s+=i
        c+=1
print(s/c)