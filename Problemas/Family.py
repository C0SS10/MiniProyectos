MOD = 1000000009

def matrixMult(A, B):
    #   Resumiendo: para encontrar el indíce requerido se hara el producto punto
    #   esto es la misma matriz multiplicada por si misma
    #   [1,1] [1,0] -> (1*1+1*1 1*1+1*0) (1*1+0*1 1*1+0*0) -> [2,1] [1,1] para ('2,3')
    #   0 + 1 = 1 -> 1 + 1 = 2 el indíce 3 de la secuencia 2 (serie tradicional de Fibonacci) es 2
    R = [[sum(a*b % MOD for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

    #   Retornamos la matriz solución
    return R

def matrixPow(k, A, b):
    # I = [[0 for col in range(k)] for row in range(k)]
    I = [[0]*k]*k

    #   Siguiendo con la matriz [1,1] [1,0]
    #   este ciclo crea una matriz I [1,1] [1,1]
    for i in range(k):
        I[i][i] = 1

    #   Si n = 0 retornamos la matriz I, el indíce 0 siempre será 1
    if (b==0): return(I)
    #   Si n = 1 retornamos la matriz A, el indíce 1 siempre será 1
    elif (b==1): return(A)

    #   Si n es par entonces se hace recursividad de matrixPow
    #   hasta que n = 0 para obtener los 0; por ejemplo
    #   0,1,1,2,3 para ('2,3') 0,0,1,1,2,4 -> (4 + 2) + 1 = 7 para ('3,4')
    #   esto es porque debemos tener en cuenta el ante-anterior
    #   el cual será; el número que sumaremos después de hacer una serie de fibonacci tradicional
    elif (b%2 == 0):
        #   Creamos una nueva matriz que será igual a [1,1] [1,0]
        #   siguiendo con el ejemplo de ('2,3')
        R = matrixPow(k, A, b/2)
        #   Retornamos la multiplicación de la misma matriz
        return(matrixMult(R , R))

    #   Si no cumple con ningún caso anterior vamos a retornar:
    #   la misma matriz multiplicada por sí misma no sin antes obtener los 0s o los 'ante-anteriores'

    #   ¡REPITE LA RECURSIVIDAD N VECES! 
    #   SI N ES 10 SE MULTIPLICA LA MISMA MATRIZ 10 VECES
    else: return(matrixMult(A, matrixPow(k, A, b-1)))

def kFibonacci(k,n):
    #   El indíce 0 y 1 de la secuencia 1 siempre será 1
    #   (secuencia '0 0' no existe)
    if (k == 1 or k == 0 or n == 1): return(1)

    #   Inicializando una matriz vacia (con 0s en las filas y columnas)
    #   El tamaño de la matriz será cuadrada 'k'
    A = [[0 for col in range(k)] for row in range(k)]

    #   Llenando las filas de la matriz con 1s
    #   El valor de la secuencia nos permite saber que si por ejemplo estamos en la secuencia
    #   número 5 habrán deberemos sumar 4 valores anteriores al indíce actual

    #   [1,1], [1,0] matriz 'A' secuencia 2 (Fibonacci tradicional)
    #   [1,1,1],[1,0,0],[0,1,0] matriz 'A' secuencia 3
    #   [1,1,1,1],[1,0,0,0],[0,1,0,0],[0,0,1,0] matriz 'A' secuencia 4
    #   [1,1,1,1,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0] matriz 'A' secuencia 5

    #   ¡¡¡(Si multiplicamos n veces alguna de las anteriores matriz KxK por si misma
    #   obtendremos el valor del indíce requerido)!!!
    for i in range(k):
        #   solo se llena la primera fila de 1s
        A[0][i] = 1
    
    #   Llenando las columnas de la matriz con 1 menos la última casilla
    for j in range(k-1):
        A[j+1][j] = 1

    #   [1 1] por ejemplo
    #   [1 0]
    #   Ans será la matriz que nos dará el indíce requerido el cual será el primer valor de la matriz
    Ans = matrixPow(k, A, n)

    print(Ans)
    return(Ans[0][0])

def solucion():

    #   Pedimos al usuario que ingrese el número de la secuencia (k)
    #   y el indice que quiere de esa secuencia (n)

    while True:
        #   ciclo infinito hasta que el usuario ingresa '0 0'
        try:
            #   El input que ingrese el usuario deberá ser: '7 0' ó '5 5'
            k, n = map(int, input('Ingrese el número de la secuencia y el indíce: ').split())

        except ValueError:
            # No es un número
            print("Input invalido")
            continue

        except EOFError:
            #   Si ha pasado mucho tiempo y no se ha ingresado una entrada
            break

        if k <= 0 and n <= 0:
            #   Si se ingresan números negativos
            break

        print(f'El indíce [{n}] de la secuencia [{k}] es: {kFibonacci(k, n)}')
    return