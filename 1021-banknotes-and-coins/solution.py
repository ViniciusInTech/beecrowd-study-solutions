from decimal import Decimal

dinheiro = Decimal(input())

notas = [
    Decimal("100"),
    Decimal("50"),
    Decimal("20"),
    Decimal("10"),
    Decimal("5"),
    Decimal("2")
]
print("NOTAS:")
for nota in notas:
    quantidade_notas = dinheiro // nota
    dinheiro = dinheiro % nota
    print(f"{quantidade_notas:.0f} nota(s) de R$ {nota:.2f}")

moedas = [
    Decimal("1.00"),
    Decimal("0.50"),
    Decimal("0.25"),
    Decimal("0.10"),
    Decimal("0.05"),
    Decimal("0.01")
]
print("MOEDAS:")
for moeda in moedas:
    quantidade_moeda = dinheiro // moeda
    dinheiro = dinheiro % moeda
    print(f"{quantidade_moeda:.0f} moeda(s) de R$ {moeda:.2f}")