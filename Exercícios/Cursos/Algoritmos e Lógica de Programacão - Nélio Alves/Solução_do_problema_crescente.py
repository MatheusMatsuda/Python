"""
Solução Própria

duplas = int(input("Digite a quantidade de duplas utilizadas: "))

for i in range(1,duplas):
    X = int(input("Digite o valor X: "))
    Y = int(input("Digite o valor Y: "))
    if X < Y:
        print("Crescente")
    elif X > Y:
        print("Decrescente")
    else:
        break

"""
print("Digite dois números: ")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    print("Digite outros dois números: ")
    x = int(input())
    y = int(input())