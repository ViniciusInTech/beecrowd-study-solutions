CONSUMO_CARRO = 12
tempo_viagem = int(input())
velocidade_viagem = int(input())

distancia_viagem = tempo_viagem * velocidade_viagem
combustivel_viagem = distancia_viagem / CONSUMO_CARRO

print(f"{combustivel_viagem:.3f}")