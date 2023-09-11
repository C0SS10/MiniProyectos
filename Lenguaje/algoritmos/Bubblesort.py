def bubbleSort(vector):
    #   Primer bucle for para acceder a todos los elementos del vector
    for i in range(len(vector)):
        #   Segundo bucle for para comparar los elementos del vector
        for j in range(0, len(vector) - i - 1):
            # Comparando dos elementos adyacentes
            # Cambiando posiciones en orden descendente
            if vector[j] > vector[j + 1]:
            # cambiando la posición de los elementos si no están en el orden correspondiente
                temp = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = temp