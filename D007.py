n = int(input())
l = list(map(int,input().split()))
ln=[]


#invertendo posições na lista par a par
if n%2 == 0 and n!=1:
    i=0
    while i<n:
        x=l[i]
        y=l[i+1]
        ln.append(y)
        ln.append(x)
        i=i+2
elif n%2 != 0 and n != 1:
    i=0
    while i<n-1:
        x=l[i]
        y=l[i+1]
        ln.append(y)
        ln.append(x)
        i=i+2
    x=l[i]
    ln.append(x)

#imprindo elementos da lista na mesma linha
i=0
if n>1:
    while i<n-1:
        print(ln[i],end=" ")
        i=i+1
    print(ln[i])
else:
    print(l[i])