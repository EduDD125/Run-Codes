n = int(input())
soma=0


if n == 0:
    soma=0
elif n>=1:
    i=1
    while n >= i:
        i=i*10
    i=i/10
    while i>=1:
        resto=n//i
        soma=soma+resto
        n=n-resto*i
        i=i/10
        
soma=int(soma)
print(soma)