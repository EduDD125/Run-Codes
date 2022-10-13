n = int(input())
l=[]


i=0
while i<n:
    x=input()
    l.append(x)
    i=i+1

i=0
a=i+1
m=0
while i<(n-1) and a<n:
    if l[i]>l[a]:
        m=int(l[i])
        a=a+1
    else:
        m=int(l[a])
        i=a
        a=a+1

i=0
a=0
while i<n and a<1:
    if l[i]==m:
        a=a+1
    else:
        i=i+1
i=i-1
print(m)
print(i)