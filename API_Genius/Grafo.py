import random

#Cadenas de markov o grafos.
class Vertice():
    def __init__(self, valor):
        self.valor = valor
        #   Necesitamos saber los nodos que tienen arista con el nodo actual
        #   esto se hace para saber el peso del nodo
        self.adyacente = {} #Dictionarie (Lista de pares)
        self.vecino = []
        self.pesos = []

    def agregar_artista(self,vertice,peso=0):
        #   agrega una arista con su respectivo peso
        self.adyacente[vertice] = peso

    def aumentar_arista(self, vertice):
        #   si el vertice enviado existe obtenemos su valor sino lo volvemos 0
        #   el get obtiene el valor 'key' si está en un Dictionarie
        self.adyacente[vertice] = self.adyacente.get(vertice,0) + 1
    
    def obtener_mapaProbabilidad(self):
        for (vertice,peso) in self.adyacente.items():
            self.vecino.append(vertice)
            self.pesos.append(peso)


    def siguiente(self):
        #   selecciona la siguiente palabra teniendo en cuenta el peso
        return random.choices(self.vecino,self.pesos)[0]


class Grafo:
    def __init__(self):
        #   inicialmente el grafo es un dictionary vacio
        #   esto nos ayuda a obtener los valores o palabras que tiene el grafo
        self.vertices = {}
    
    def obtener_valor_vertice(self):
        #   valores de todos los vertices
        return set(self.vertices.keys())

    def agregar_vertice(self,valor):
        self.vertices[valor] = Vertice(valor)

    def obtener_vertice(self, valor):
        #   si el vertice no existe, lo agregamos
        if valor not in self.vertices:
            self.agregar_vertice(valor)
        #   obtiene el objeto vertice
        return self.vertices[valor]

    def obtener_siguiente_nodo(self,actual_vertice):
        self.vertices[actual_vertice.valor].siguiente()

    def generar_mapasProbabilidad(self):
        #   para cada vertice se hará un mapa de probabilidad
        for vertice in self.vertices.values():
            vertice.obtener_mapaProbabilidad()