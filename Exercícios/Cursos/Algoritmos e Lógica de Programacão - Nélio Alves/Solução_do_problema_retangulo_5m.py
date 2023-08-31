"""
#Solução própria

import math

baseRetangulo = float(input("Digite o a medida da base do retangulo: "))
alturaRetangulo = float(input("Digite o a medida da altura do retangulo: "))

#Área = base x altura
areaRetangulo = baseRetangulo * alturaRetangulo

#Perímetro = 2 x (base + altura)
perimetroRetangulo = 2 * (baseRetangulo + alturaRetangulo)

#Diagonal = √(base² + altura²)
diagonalRetangulo = math.sqrt(baseRetangulo ** 2 + alturaRetangulo ** 2)

print(f"A área do retangulo ínformado é: {areaRetangulo:.4f}")
print(f"O perimetro do retangulo ínformado é: {perimetroRetangulo:.4f}")
print(f"A diagonal do retangulo ínformado é: {diagonalRetangulo:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
"""

import math

base = float(input("Base do Retangulo: "))
altura = float(input("Altura do Retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
