# programa para ler dois valor, calcular e imprimir seu maximo divisor comum usando algoritmo de euclides

a = int(input())
b = int(input())
resto=1

if a>b:
    while resto > 0:
        resto = a%b
        a=b
        b=resto
    mdc=a
elif a<b:
    while resto > 0:
        resto= b%a
        b=a
        a=resto
    mdc=b
else:
    mdc=a

print(mdc)
