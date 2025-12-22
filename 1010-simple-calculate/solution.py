codigo_produto_1, quantidade_produto_1, valor_produto_1 = input().split()
codigo_produto_2, quantidade_produto_2, valor_produto_2 = input().split()

total_produto_1 = int(quantidade_produto_1) * float(valor_produto_1)
total_produto_2 = int(quantidade_produto_2) * float(valor_produto_2)
valor_total = total_produto_1 + total_produto_2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")