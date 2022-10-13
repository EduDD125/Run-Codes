n = int(input())


i=1
soma=0
while i<=n:
    a=1
    d=0
    while a<=i:
        if i%a == 0:
            d=d+1
        a=a+1
    if d == 2:
        soma=soma+i
    i=i+1

print(soma)