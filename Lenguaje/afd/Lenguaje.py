import re
import random

#   Expresión regular que deben cumplir las cadenas
e_r = r'(0*1(01)*0*)*'

def generarLenguaje():
    #   Retornamos una lista (Lenguaje) de 10 palabras 
    L = []
    #   Para no repetir palabras
    palabras_usadas = set()
    while len(L) < 10:
        palabra = "".join([random.choice(["0", "1"]) for j in range(random.randint(1, 10))])
        if re.fullmatch(e_r, palabra) and palabra not in palabras_usadas:
            L.append(palabra)
            palabras_usadas.add(palabra)
    return L