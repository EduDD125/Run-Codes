n=int(input())


if n>0:
    a=1
    soma=0
    while a<=n:
        i=a
        f=1
        while i>0:
            f=f*i
            i=i-1
        soma=soma+f
        a=a+1
    soma=soma+1
else:
    soma=1



print(soma)