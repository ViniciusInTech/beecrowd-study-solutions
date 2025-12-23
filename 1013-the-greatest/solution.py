def maior_numero(numero_a: int, numero_b: int) -> int:
    if numero_a > numero_b:
        return numero_a
    return numero_b

a, b, c = map(int, input().split())
primeiro_resultado = maior_numero(a, b)
resultado_final = maior_numero(primeiro_resultado, c)
print(f"{resultado_final} eh o maior")
