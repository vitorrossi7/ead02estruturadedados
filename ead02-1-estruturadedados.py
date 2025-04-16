soma = 0
n = int(input('Digite um número inteiro e positivo: '))

for c in range(1, n + 1):
    soma += 1 / c

print(f'A soma é {soma:.2f}')