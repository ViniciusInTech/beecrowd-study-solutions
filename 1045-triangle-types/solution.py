lados = list(map(float, input().split()))
lados.sort(reverse=True)

a, b, c = lados

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    a_quadrado = a ** 2
    soma_dos_quadrados = (b ** 2) + (c ** 2)

    if a_quadrado == soma_dos_quadrados:
        print("TRIANGULO RETANGULO")
    elif a_quadrado > soma_dos_quadrados:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c:
        print("TRIANGULO ISOSCELES")
