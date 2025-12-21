empregado_id = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora
print(f"NUMBER = {empregado_id}")
print(f"SALARY = U$ {salario:.2f}")