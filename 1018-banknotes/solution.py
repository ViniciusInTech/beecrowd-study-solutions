valor_pedido = int(input())
print(valor_pedido)

qtd_notas_100 = valor_pedido // 100
valor_pedido = valor_pedido % 100

qtd_notas_50 = valor_pedido // 50
valor_pedido = valor_pedido % 50

qtd_notas_20 = valor_pedido // 20
valor_pedido = valor_pedido % 20

qtd_notas_10 = valor_pedido // 10
valor_pedido = valor_pedido % 10

qtd_notas_5 = valor_pedido // 5
valor_pedido = valor_pedido % 5

qtd_notas_2 = valor_pedido // 2
valor_pedido = valor_pedido % 2

qtd_notas_1 = valor_pedido // 1
valor_pedido = valor_pedido % 1

print(f"{qtd_notas_100} nota(s) de R$ 100,00")
print(f"{qtd_notas_50} nota(s) de R$ 50,00")
print(f"{qtd_notas_20} nota(s) de R$ 20,00")
print(f"{qtd_notas_10} nota(s) de R$ 10,00")
print(f"{qtd_notas_5} nota(s) de R$ 5,00")
print(f"{qtd_notas_2} nota(s) de R$ 2,00")
print(f"{qtd_notas_1} nota(s) de R$ 1,00")