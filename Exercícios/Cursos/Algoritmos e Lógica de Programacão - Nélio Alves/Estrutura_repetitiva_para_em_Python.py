"""
or i in range(0, 5):
    print(i)
"""

"""
for i in range(0, 5, 2):
    print(i)
"""

"""
N = int(input("Quantos números serão digitados ?"))
for i in range(1, N+1):
    (input(f"Digite o {i}º número:"))
"""

N = int(input("Quantos números serão digitados ?"))

soma = 0
for i in range(0, N):
    x = int(input("Digite um numero"))
    soma = soma + x

print("SOMA = ", soma)