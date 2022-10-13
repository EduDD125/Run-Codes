from re import X


x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

#condições para acontecer encontro
      # v1 e v2 são como a tangente da reta das funções representantes do movimento dos cangurus
      # logo,1) v1 > v2 e x1 > x2 ou 2) v2 > v1 e x2 > x1 nunca haverá encontro

if x1 > x2 and v1 < v2:
    print("SIM")

elif x1 < x2 and v1 > v2:
    print("SIM")
elif x1 == x2 and v1 == v2:
    print("SIM")
else:
    print("NAO")