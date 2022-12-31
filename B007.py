# Programa para recer numeros inteiros e imprimir estes em ordem crescente.

# ENTRADA:
a = int(input())
b = int(input())

# PROCESSAMENTO:
if a > b:
    c = a
    a = b
    b = c

# SAIDA:
print(a)
print(b)
