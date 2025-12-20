A_PESO = 2
B_PESO = 3
C_PESO = 5

a = float(input())
b = float(input())
c = float(input())

media = (a * A_PESO + b * B_PESO + c * C_PESO) / (A_PESO + B_PESO + C_PESO)
print(f"MEDIA = {media:.1f}")