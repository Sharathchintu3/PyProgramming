def minlen(l,t):
    s, ml,le, r= 0, 10**6, 0, 0
    while r<len(l):
        s+=l[r]
        while s>=t:
            ml=min(r-le+1, ml)
            s-=l[le]
            le+=1
        r+=1
    return ml
l = [2,3,1,4,3,5,8,2]
t = 10
print(minlen(l,t))