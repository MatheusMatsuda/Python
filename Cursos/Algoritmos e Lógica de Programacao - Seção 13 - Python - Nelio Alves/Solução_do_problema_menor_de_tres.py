""""
Solução própria

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero "))

if n1 < n2 and n1 < n3:
    print(f"O menor número é {n1}")
elif n2 < n1 and n2 <n3:
    print(f"O menor número é {n2}")
else:
    print(f"O menor número é {n3}")
"""

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor "))


if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c

print(f"Menor = {menor}")