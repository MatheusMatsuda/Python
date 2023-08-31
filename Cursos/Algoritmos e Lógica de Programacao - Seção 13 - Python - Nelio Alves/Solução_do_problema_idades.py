"""
#Solucão própria

nome1 = input("Digite o nome da pessoa 1: ")
idade1 = int(input("Digitie a idade da pessoa 1: "))
nome2 = input("Digite o nome da pessoa 2: ")
idade2 = int(input("Digitie a idade da pessoa 2: "))

mediaIdade = (idade1 + idade2) / 2

print(f"A pessoa 1 se chama {nome1} e a pessoa 2 se chama {nome2} a média das idades das duas pessoas é {mediaIdade} ")
"""

print("Dados da primeira pessoa")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade média de {nome1} e {nome2} é de {media:.1f} anos")
