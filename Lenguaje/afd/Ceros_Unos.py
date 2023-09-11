#   Elaborar un programa que nos permita simular un AFD que reconozca
#   una secuencia de ceros pares o unos impares.

def reconocerSecuencia(entrada):
    estado = 0
    
    # La cadena se acepta si tiene ceros y unos
    # Si tiene un número par de 0 y par de 1
    # Si tiene un número par de 0 e impar de 1
    # Si tiene un número impar de 0 e impar de 1

    for char in entrada:
        if estado == 0:
            if char == '0':
                estado = 1
            elif char == '1':
                estado = 2
            else:
                return False
        elif estado == 1:
            if char == '0':
                estado = 0
            elif char == '1':
                estado = 3
            else:
                return False
        elif estado == 2:
            if char == '0':
                estado = 3
            elif char == '1':
                estado = 0
            else:
                return False
        elif estado == 3:
            if char == '0':
                estado = 2
            elif char == '1':
                estado = 1
            else:
                return False
            
    return estado in [0, 2, 3]