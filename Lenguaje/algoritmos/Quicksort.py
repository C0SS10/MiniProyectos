#   Método para obtener el indice del pivote
def particion(vector,inicio,final):
    p = vector[final]
    i = inicio - 1
    for j in range(inicio,final):
        #   se mueven los elementos menores que el pivote a la izquierda
        if vector[j] <=  p:
            i += 1
            (vector[i], vector[j]) = (vector[j], vector[i])
    #   se mueve el pivote a su posición correspondiente
    (vector[i + 1], vector[final]) = (vector[final], vector[i + 1])
    return i + 1

#   Ordenamiento rápido utilizando recursividad
def quickSort(vector, inicio, final):
    #   inicio y final son los indices del vector inicio = 0 y final = n - 1
    if inicio < final:
        #   obtenemos el indice del pivote
        pivote = particion(vector,inicio,final)

        #   se llama el método quickSort de inicio a pivote - 1
        #   esto es para ordenar la sublista izquierda
        quickSort(vector,inicio,pivote-1)
        #   se llama el método quickSort de pivote + 1 a final
        #   esto es para ordenar la sublista derecha
        quickSort(vector,pivote+1,final)