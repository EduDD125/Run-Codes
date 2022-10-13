n=float(input())
c=float(input())
m=int(input())

compra=n//c
troca = compra//m
soma=compra+troca

while troca>0:
    troca=troca//m
    soma=soma+troca

print(soma)