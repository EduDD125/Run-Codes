n=int(input())

i=0
while i<1:
    m=int(input())
    i=i+1
    while i<n:
        x=int(input())
        if x>m:
            m=x
            i=i+1
        else:
            i=i+1
print(m)