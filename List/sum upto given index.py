l = list(map(int, input().split()))
key = int(input())
s = 0
for i in range(0, key+1):
    s += l[i]
print(s)

# or

su = 0
a = l[0:key+1]
for i in a:
    su+=i
print(s)