n=int(input())
l = list(map(int,input().split()))
ln=[]

#montando lista nova com ordem dos números invertidas
i=-1
while i>=n*(-1):
    x=l[i]
    ln.append(x)
    i=i-1

#imprimindo numeros da lista invertidas em uma única linha
i=0
while i<n:
    while i<(n-1):
        print(ln[i],end=" ")
        i=i+1
    print(ln[i])
    i=i+1

