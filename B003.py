i=int(input())

if i>69:
    print("DISPENSADO")
elif i>=18:
    print("OBRIGATORIO")
elif 16<=i and i<=17:
    print("FACULTATIVO")
else:
    print("DISPENSADO")