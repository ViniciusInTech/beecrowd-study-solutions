a, b, c, d = map(int,input().split())

condicao_1 = b > c and d > a
condicao_2 = (c + d) > (a + b)
condicao_3 = c >= 0 and d >= 0
condicao_4 = a % 2 == 0

if condicao_1 and condicao_2 and condicao_3 and condicao_4:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")