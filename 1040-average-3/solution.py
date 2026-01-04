nota1, nota2, nota3, nota4 = map(float, input().split())
peso1, peso2, peso3, peso4 = 2, 3, 4, 1

media = (
    (nota1 * peso1) +
    (nota2 * peso2) +
    (nota3 * peso3) +
    (nota4 * peso4)
) / (peso1 + peso2 + peso3 + peso4)

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_recuperacao = float(input())
    print(f"Nota do exame: {nota_recuperacao:.1f}")
    media_final = (media + nota_recuperacao) / 2
    print(f"Aluno aprovado." if media_final >= 5 else "Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")


