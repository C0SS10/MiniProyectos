import random

#   No es necesario ya que python cuenta con sorted() una funcion que ordena listas
#   Como práctica para crear listas con valores aleatorios (- y +) y posteriormente ordenarlos

def mezclar():
    tamaño = random.randint(2, 50)
    arr = [0] * tamaño
    for i in range(tamaño):
        arr[i] = (random.randint(-1*100,1*100))
    print(f'La lista inicial es: {arr}', end='\n')
    print()
    l = mergesort(arr)
    print(f"La lista organizada de tamaño ({tamaño}) es: {l}", end="\n")

def mergesort(l):
    if len(l) > 1:
        puntomedio = len(l)//2
        bajo = l[:puntomedio] # todos los valores a la izquierda del punto medio
        alto = l[puntomedio:] # todos los valores a la derecha del punto medio
        
        #Recursividad
        mergesort(bajo)
        mergesort(alto)

        #Variables para remplazar posiciones
        i = j = k = 0
        while i < len(bajo) and j < len(alto):
            #   si el valor que está a la derecha de la posicion inicial es mayor
            #   colocamos el valor menor al inicio de la lista
            if bajo[i] <= alto[j]:
                l[k] = bajo[i]
                i += 1
            else:
                l[k] = alto[j]
                j += 1
            k += 1
        
        #Se revisa si todos los valores están bien colocados
        while i < len(bajo):
            l[k] = bajo[i]
            k += 1
            i += 1
        while j < len(alto):
            l[k] = alto[j]
            k += 1
            j += 1

    #Retornamos una lista ordenada
    return l