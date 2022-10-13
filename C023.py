idade = int(input())


velas = []
i=0
while  i < idade:
    x = float(input())
    velas.append(x)
    i = i + 1

maior = 0
i = 0
while i < len(velas):
    if velas[i]>maior:
        maior = velas[i]
    i = i + 1



quant_maiores = 0
i = 0
while i < len(velas):
    if velas[i] == maior:
        quant_maiores = quant_maiores + 1
    i = i+ 1

print(quant_maiores)