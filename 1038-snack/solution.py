cardapio = {
    1:4.0,
    2:4.5,
    3:5,
    4:2,
    5:1.5
}
codigo, quantidade = map(int, input().split())

valor_pedido = cardapio.get(codigo) * quantidade
print(f"Total: R$ {valor_pedido:.2f}")