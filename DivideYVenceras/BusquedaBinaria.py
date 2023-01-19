import random
import time

#   Implementación de la busqueda binaria
#   La busqueda binaria es más eficiente que la busqueda sencilla de strings

def buscar():
    tamaño = 1000
    l_ord = set()

    while len(l_ord) < tamaño:
        l_ord.add(random.randint(-3*tamaño,3*tamaño))
    
    l_ord = sorted(list(l_ord))
    start = time.time()

    for objetivo in l_ord:
        busqueda_sencilla(l_ord,10)
    end = time.time()
    #Tiempo por cada iteración
    print("Tiempo de ejecución busqueda sencilla: ",(end-start)/tamaño,"Segundos")

    for objetivo in l_ord:
        busqueda_binaria_ordenada(l_ord,10)
    end = time.time()
    #Tiempo por cada iteración
    print("Tiempo de ejecución busqueda binaria: ",(end-start)/tamaño,"Segundos")

def busqueda_sencilla(l,objetivo):
    for i in range(len(l)):
        if l[i] == objetivo:
            #return print(f' La posición del objetivo es {i}')
            return i
    
    return -1

#   Divide y venceras, está técnica es usada por el algoritmo de busqueda binaria
def busqueda_binaria_ordenada(l,objetivo,bajo = None, alto = None):
    if bajo is None:
        bajo = 0
    if alto is None:
        alto = len(l)-1 #   la lista tiene 6 indices (7-1)

    #   si el objetivo no existe; que alto < bajo no va a pasar nunca a menos que...
    if alto < bajo:
        return -1

    puntomedio = (bajo+alto)//2 # 3 en una lista de 7 valores
    #   si el punto medio es igual a nuestro objetivo
    if l[puntomedio] == objetivo:
        #return print(f' La posición del objetivo es {puntomedio}')
        return puntomedio

    #   si el punto medio es menor que el objetivo buscamos hacia la izquierda
    elif objetivo < l[puntomedio]:
        return busqueda_binaria_ordenada(l,objetivo,bajo,puntomedio-1)

    #   si el punto medio es mayor que el objetivo buscamos hacia la derecha
    else:
        return busqueda_binaria_ordenada(l,objetivo,puntomedio+1,alto)