"""
#Solução pessoal
soma = 0

print("Digite dois números:")
X = int(input("X: "))
Y = int(input("Y: "))

for i in range(X + 1,Y):
    if i % 2 != 0:
        soma = soma + i

print(f"O resultado a soma é {soma}")
"""

print("Digite dois números:")
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + i

print(f"SOMA DOS IMPARES = {soma}")

