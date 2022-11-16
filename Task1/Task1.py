n,m = input().split()
n=int(n)
m=int(m)
a=[]
k=1
for i in range(n):
    a.append(k)
    k += 1
c=[a[0]]
p=0
e=[]
f=0
d=m
b=a
while f != 1:
    b+=a
    for i in range(p,p+m):
        e.append(b[i])
    c.append(e[d-1])
    d+=m
    p += (m - 1)
    f=int(c[-1])
top=c.pop()
print(c)