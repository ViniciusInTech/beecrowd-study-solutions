a, b = map(float, input().split())

def ordenar_numero(x, y):
    if x > y:
        return x, y
    return y, x

a, b = ordenar_numero(a, b)
divisao = a / b
if divisao == int(divisao):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
