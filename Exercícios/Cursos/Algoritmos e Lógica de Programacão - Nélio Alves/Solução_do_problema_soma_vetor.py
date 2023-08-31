#Solução própria

"""
soma: float = 0

N = int(input("Quantos numeros voce vai digitar:  "))

vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

print("")
print("Todos elementos do vetor")
for i in range(0,N):
    print(f"{vet[i]:.2f}")

for i in range(0,N):
    soma = soma + vet[i]

media = soma / N

print(f"Soma dos elementos do vetor: {soma}")

print(f"Média dos elementos do vetor: {media}")
"""

N = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

print()
print("VALORES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f}  ", end="")

print()

soma = 0
for i in range(0,N):
    soma = soma + vet[i]

print(f"SOMA = {soma:.2f}")

media = soma / N
print(f"MEDIA = {media:.2f}")

