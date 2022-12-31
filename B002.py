# Calcaular valor de multa de transito - com taxa de acrescimo para a diferença da velocidade do carro em relação com a velocidade máxima

velocidade_max = int(input())
multa_min = float(input())
taxa = float(input())
velocidade_carro=int(input())

multa=m+a*(v-l)

if velocidade_carro > velocidade_max:
    multa = multa_min + taxa * (velocidade_carro - velocidade_max)
    print(f"{multa:.2f}")
else:
    multa=0
    print(f"{multa:.2f}")
