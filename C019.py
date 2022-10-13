a=int(input())
b=int(input())
resultado=0
n=a

if b>1:
    i=0
    while i<b-1:
        d=0
        resultado=0
        while d<a:
            resultado=resultado + n
            d=d+1
        i=i+1
        n=resultado
elif b==1:
    resultado = a
else:
    resultado = 1
print(resultado)

