import string
import random
import re
import os

from API_Genius.Grafo import Grafo,Vertice

def leer_txt(direccion):
    with open(direccion,'r') as f:
        #   Leyendo el texto y guardandolo como un string
        texto = f.read()
        #   Quitar los corchetes de cada letra como [Chorus]
        #   '.' cualquier carácter, '+' uno o más
        texto = re.sub(r'\[(.+)\]',' ', texto)
        #   Los espacios exagerados se convierten en uno solo
        #   'Este   es  el   texto' -> 'Este es el texto'
        texto = ' '.join(texto.split())
        texto = texto.lower() # minisculas
        #   Tendremos que cambiar '¡Ahí está! por Ahi esta
        texto = texto.translate(str.maketrans('','',string.punctuation))

    #   se separan las palabras
    palabras = texto.split()
    return palabras

def crear_grafo(palabras):
    g = Grafo() #Nuevo grafo

    palabra_anterior = None #   al principio casi todas las palabras son nuevas

    #   se debe revisar si la palabra está en el grafo si no, se agrega
    for palabra in palabras:
        palabra_vertice = g.obtener_vertice(palabra)

        #   si ya estaba en el grafo le agregamos una arista o aumentamos el peso de la arista
        if palabra_anterior:
            palabra_anterior.aumentar_arista(palabra_vertice)

        palabra_anterior = palabra_vertice

    g.generar_mapasProbabilidad()

    return g

def construir(grafo,palabras,tamaño):
    construccion = []
    palabra = grafo.obtener_vertice(random.choice(palabras))

    for _ in range(tamaño):
        construccion.append(palabra.valor)
        palabra = grafo.obtener_siguiente_nodo(palabra)

    return construccion

def componer(artista):
    #   primer paso: obtener las palabras con las que trabajaremos
    palabras = []

    for canciones in os.listdir(f'API_Genius/canciones/{artista}'):
        barras = leer_txt(f'API_Genius/canciones/{artista}/{canciones}')
        palabras.extend(barras)

    #   segundo paso: construir el grafo con las palabras
    g = crear_grafo(palabras)
    #   tercer paso: construirmos la cadena de Markov
    composicion = construir(g,palabras,100)
    return ' '.join(composicion)