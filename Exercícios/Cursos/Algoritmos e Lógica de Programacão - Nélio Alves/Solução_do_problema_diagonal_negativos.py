"""
#Solução pessoal

contadorNegativos = 0

while True:
    N = int(input("Qual será a ordem da Matriz? (Máximo 10): "))
    if N > 10:
        continue
    else:
        break

diagonalPrincipal = [0 for x in range(N)]

M = N

mat = [[0 for x in range(N)] for y in range(M)]

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
        if mat[i][j] < 0:
            contadorNegativos = contadorNegativos + 1
        if i == j:
            diagonalPrincipal[i] = mat[i][j]

print("")
print("MATRIZ DIGITADA:")
for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")
    print()

print("")
print(f"QUANTIDADE DE NEGATIVOS: {contadorNegativos}")
print("")
print(f"DIAGONAL PRINCIPAL: {diagonalPrincipal}")
"""

N = int(input("Qual será a ordem da Matriz? "))

mat = [[0 for X in range(N)] for X in range(N)]

for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento0 [{i},{j}] "))

print("DIAGONAL PRINCIPAL")
for i in range(0, N):
    print(f"{mat[i][i]} ",  end="")
print()

cont = 0
for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] < 0:
            cont = cont + 1

print(f"QUANTIDADE DE NEGATIVOS = {cont}")
