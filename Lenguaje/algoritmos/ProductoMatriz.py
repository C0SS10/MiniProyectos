def multiplicarMatrices(A, B):
    filas_a = len(A)
    filas_b = len(B)
    columnas_a = len(A[0])
    columnas_b = len(B[0])
    #   Condición para saber si las matrices se pueden multiplicar
    if columnas_a != filas_b:
        return None

    # Creando la matriz producto con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)

    # Rellenar la matriz producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += A[i][j]*B[j][c]
            producto[i][c] = suma
    
    #   Retorna la matriz producto
    return producto