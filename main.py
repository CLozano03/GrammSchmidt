import time

dimension = 0
numero_vectores = 0

while dimension <= 0 or dimension > 5:
    try:
        dimension = int(input("Escribe el tamanio de la dimension de la base B (entre 0 y 6, no incluidos): "))
    except ValueError:
        print("ERROR, no se trata de un numero valido")

while numero_vectores <= 0 or numero_vectores > dimension:
    try:
        numero_vectores = int(input("Escribe el numero de vectores de tu base:  "))
    except ValueError:
        print("ERROR, no se trata de un numero valido")


def producto_escalar(v1, v2):
    pdtoescalar = 0
    for x in range(dimension):
        pdtoescalar += v1[x] * v2[x]
    return pdtoescalar


def grammSchmidt(matriz):
    matriz_ortogonal = [[0 for x in range(dimension)] for y in range(dimension)]

    for fila in range(dimension):  # Asignacion primer vector
        matriz_ortogonal[0][fila] = matriz[0][fila]
    if dimension > 1:
        for columna in range(1, numero_vectores):  # Resto de vectores
            for fila in range(dimension):
                matriz_ortogonal[columna][fila] = matriz[columna][fila]
                for subindice in range(columna):
                    matriz_ortogonal[columna][fila] -= ((producto_escalar(matriz[columna], matriz_ortogonal[
                        subindice]) / producto_escalar(matriz_ortogonal[subindice], matriz_ortogonal[subindice])) *
                                                        matriz_ortogonal[subindice][fila])
        return matriz_ortogonal


base_B = [[0 for x in range(dimension)] for y in range(dimension)]
elemento = 0

for col in range(numero_vectores):
    # Pido al usuario que ingrese la base
    print("Ingresa el vector numero " + str(col + 1) + " de tu base B: ")
    for coordenada in range(dimension):
        elemento = int(input())
        base_B[col][coordenada] = elemento

print("Tu base B: \n" + str(base_B))
print("Base ortogonalizada: ")
print("\n")
print(grammSchmidt(base_B))
