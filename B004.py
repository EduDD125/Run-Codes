# Calcular valor de corrida com diferentes taxas dependedo das distancia percorrida. Valor acima de "distancia_taxa" teram um taxa 'taxa_1' e a baixo teram um taxa 'taxa_2'

distancia_taxa=float(input())
taxa_1 = float(input())
taxa_2 = float(input())
distancia_percorrida=float(input())

if distancia_percorrida <= distancia_taxa:
   valor = distancia_percorrida * taxa_1
else:
    valor = distancia_percorrida * taxa_2
print(f"{valor:.2f}")
