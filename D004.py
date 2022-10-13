n = int(input())
l = list(map(int,input().split()))
x=int(input())

i=0
a=0
while i<n and a<1:
    if l[i]==x:
        a=a+1
    else:
        i=i+1

if a==1:
    print(i)
else:
    print("-1")