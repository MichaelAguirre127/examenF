laberinto = [
    ["F", 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ["I", 1, -1, 1, 1, 1, 0, 1, 1]
]

N = 9

visitado = [[False]*N for _ in range(N)]
solucion = [[0]*N for _ in range(N)]

filas = [1, 0, -1, 0]
columnas = [0, 1, 0, -1]


def es_valido(f, c):
    return 0 <= f < N and 0 <= c < N


def backtracking(f, c, vidas):

    print("Posicion:", f, c, "Vidas:", vidas)

    if f == 0 and c == 0:
        solucion[f][c] = 1
        return True

    visitado[f][c] = True
    solucion[f][c] = 1

    for i in range(4):

        nf = f + filas[i]
        nc = c + columnas[i]

        if es_valido(nf, nc) and not visitado[nf][nc]:

            valor = laberinto[nf][nc]

            if valor == 0:
                continue

            nuevas_vidas = vidas

            if valor == -1:
                nuevas_vidas -= 1

            elif valor == -2:
                nuevas_vidas -= 2

            if nuevas_vidas > 0:

                if backtracking(nf, nc, nuevas_vidas):
                    return True

    solucion[f][c] = 0
    visitado[f][c] = False

    return False


print("Laberinto original")

for fila in laberinto:
    print(fila)

print("\nBuscando salida\n")

if backtracking(8, 0, 3):

    print("\nSalida encontrada\n")

    print("Matriz de solucion")

    for fila in solucion:
        print(fila)

else:

    print("\nNo existe camino valido")