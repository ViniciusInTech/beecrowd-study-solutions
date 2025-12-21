PORCENTAGEM_COMISSAO = 15
funcionario_nome = input()
salario_base = float(input())
total_vendas_mensal = float(input())

comissao = (total_vendas_mensal * PORCENTAGEM_COMISSAO)/100
salario = salario_base + comissao

print(f"TOTAL = R$ {salario:.2f}")