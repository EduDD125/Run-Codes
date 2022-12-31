# Terminar o comprimisso eleitoral do cidadão a partir de sua idade

idade = int(input())

if idade > 69:
    print("DISPENSADO")
elif idade >= 18:
    print("VOTO OBRIGATORIO")
elif idade >= 16 and idade <= 17:
    print("VOTO FACULTATIVO")
else:
    print("DISPENSADO")
