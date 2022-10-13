n = int(input())
l = list(map(int,input().split()))
x = int(input())

i=0
a=0
while i<n:
    if l[i]==x:
        a=a+1
    i=i+1

print(a)