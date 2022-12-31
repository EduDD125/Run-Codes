# Determinar se o ano é bissexto. verdade = 1; falso = 0 e entrada invalidade = 0

ano = int(input())


if ano <= 0:
    print(-1)
elif ano%400==0:
    print(1)
elif ano%4==0:
    if ano%100==0:
        print(0)
    else:
        print(1)
else:
    print(0)
