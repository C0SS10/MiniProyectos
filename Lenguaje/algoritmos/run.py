import random
import time
import Quicksort as Q
import Bubblesort as B
import ProductoMatriz as P

def construirVector(n):
    v = [0] * n
    for i in range(n):
        v[i] = (random.randint(1,1*100))
    return v

def construirMatrices(n):
    matriz = []
    for r in range(n):
        fila = []
        for c in range(n):
            fila.append(random.randint(0,9))
        matriz.append(fila)
    return matriz

if __name__ == '__main__':
    #   -----------------------QUICKSORT---------------------------
    n = int(input('Ingrese el tamaño del vector: '))
    v = construirVector(n)
    tamaño = len(v)
    print(f'El vector aleatorio de tamaño {n} es: {v}\n')
    start = time.time()
    Q.quickSort(v,0,tamaño-1)
    end = time.time()
    print(f'Vector ordenado usando QuickSort: {v}\n')
    t = end-start
    print(t)

    #   -----------------------BUBBLESORT--------------------------
    v = construirVector(n)
    print(f'El vector aleatorio de tamaño {n} es: {v}\n')
    start = time.time()
    B.bubbleSort(v)
    end = time.time()
    print(f'Vector ordenado usando BubbleSort: {v}\n')
    t = end-start
    print(t)

    #   -----------------------PRODUCTO MATRICES-------------------
    n = int(input('Ingrese el tamaño de las matrices (cuadradas): '))
    A = construirMatrices(n)
    B = construirMatrices(n)
    print(f'La matriz A de tamaño {n}*{n} es: {A}\n')
    print(f'La matriz B de tamaño {n}*{n} es: {B}\n')
    start = time.time()
    C = P.multiplicarMatrices(A,B)
    end = time.time()
    print(f'Resultado producto entre matrices: {C}\n')
    t = end-start
    print(t)