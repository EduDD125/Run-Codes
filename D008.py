n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []

i=0
while i<n:
    x = int(a[i]) + int(b[i])
    c.append(x)
    i=i+1

i=0
if n>1:
    while i<n-1:
        print(c[i],end=" ")
        i=i+1
    print(c[i])
else:
    print(c[i])