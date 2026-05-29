import random

def contar_multiplos(lista):
    if len(lista) == 0:
        return 0

    if len(lista) == 1:
        if lista[0] % 5 == 0 or lista[0] % 7 == 0:
            return 1
        return 0
    mitad = len(lista) // 2

    izquierda = contar_multiplos(lista[:mitad])
    derecha = contar_multiplos(lista[mitad:])
    return izquierda + derecha

n = int(input("Ingrese el tamaño de la matriz NxN: "))

matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        fila.append(random.randint(99, 999))
    matriz.append(fila)

print("\nMATRIZ GENERADA:\n")

for fila in matriz:
    for numero in fila:
        print(numero, end="\t")
    print()

elementos = []

for fila in matriz:
    for numero in fila:
        elementos.append(numero)

cantidad = contar_multiplos(elementos)

print("\nCantidad de números múltiplos de 5 o 7:", cantidad)