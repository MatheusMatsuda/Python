N = int(input("Quantos numeros voce vai digitar ? "))

vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

print("")
print("Números Digitados")
for i in range(0,N):
    print(f"{vet[i]:.1f}")