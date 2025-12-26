segundos_totais = int(input())

horas = segundos_totais // 3600
segundos_totais = segundos_totais % 3600

minutos = segundos_totais // 60
segundos_totais = segundos_totais % 60

print(f"{horas}:{minutos}:{segundos_totais}")