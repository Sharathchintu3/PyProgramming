def kdistinctsub(s: str, k: int ):
    l, r, c = 0, 0, 0
    d = {}
    while r<len(s):
        ri=s[r]
        d[ri]=d.get(ri, 0)+1
        while len(d)>k:
            li = s[l]
            d[li]= d.get(li)-1
            if d[li]==0:
                d.pop(li)
            l+=1
        c+=(r-l+1)
        r+=1
    return c
s = input()
k = int(input())
print(kdistinctsub(s, k))