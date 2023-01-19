import math
import random

#Esto es una super clase. ¡Es lo primero que se hace!
class Jugador:
    #La clase se inicializa con el simbolo de el jugador
    def __init__(self, sym):
        #Puede ser 'X' o 'O'
        self.sym = sym

    #Para saber el movimiento del jugador
    def obtener_mvto(self, juego):
        pass

class JugadorComputadora(Jugador):
    def __init__(self, sym):
        super().__init__(sym)
    
    def obtener_mvto(self, juego):
        #Elige un lugar valido y disponible para el siguiente movimiento
        cuadro = random.choice(juego.mvto_disponible())
        return cuadro

class JugadorHumano(Jugador):
    def __init__(self, sym):
        super().__init__(sym)

    def obtener_mvto(self, juego):
        cuadro_valido = False
        val = None
        while not cuadro_valido: 
            cuadro = input(self.sym+': tu turno. Movimiento (0-8): ')

            #Las excepciones serán las siguientes:
            #Tomaremos el valor del jugadorHumano mediante números enteros
            #Si el no es un número entero, el movimiento será invalidado
            #Si el lugar no está disponible o valido el movimiento será invalidado

            try:
                val = int(cuadro)
                if val not in juego.mvto_disponible():
                    raise ValueError
                cuadro_valido = True
            except ValueError:
                print('Movimiento invalido. Intenta de nuevo.')
            
        return val

class ComputadoraGenio(Jugador):
    #Utilizando el algoritmo de minimax
    def __init__(self, sym):
        super().__init__(sym)

    def obtener_mvto(self, juego):
        #Para cuando empiece el juego
        if len(juego.mvto_disponible()) == 9:
            cuadro = random.choice(juego.mvto_disponible())
        else:
            #Una vez empezado el juego, utilizamos el algoritmo de minimax
            cuadro = self.minimax(juego,self.sym)['posicion']

        return cuadro
    
    def minimax(self, estado, jugador):
        #  el estado representa las posibles imagenes del escenario
        max_j = self.sym #este va a ser el jugador humano
        min_j = 'O' if jugador == 'X' else 'X' #   máquina

        #  debemos saber si el siguiente movimiento que se hace es el ganador.
        #  primero debemos tener el caso base
        if estado.actual_ganador == min_j:
            #   retornamos posición y puntuación
            return {'posicion': None, 
                'puntuacion': 1*(estado.numero_cuadros_vacios() + 1)
                if min_j == max_j else -1*(estado.numero_cuadros_vacios() + 1)}
                #   se está retornando un 'dictionaries'
        
        #Si no hay ganador pero hay cuadros vacios
        elif not estado.cuadros_vacios():
           return {'posicion': None, 'puntuacion': 0}
        
        if jugador == max_j:
            #   Necesitamos una puntuación que podamos maximizar
            mejor = {'posicion': None, 'puntuacion': -math.inf} #inicializado en -infinity
        else:
            #   Minimizamos la puntuación
            mejor = {'posicion': None, 'puntuacion': math.inf}

        for posible_mvto in estado.mvto_disponible():
            # Para cada posible mvto en los movimientos disponibles
            #   Primero: hacemos un movimiento
            estado.hacer_mvto(posible_mvto, jugador)

            #   Segundo: recursivamente utilizamos minimax para simular despues de hacer tal mvto
            sim_puntos = self.minimax(estado,min_j)

            #   Tercero: Deshacemos el anterior movimiento
            estado.tablero[posible_mvto] = ' '
            estado.actual_ganador = None
            sim_puntos['posicion'] = posible_mvto

            #   Cuarto: Actualizamos los 'dictionarie' si es necesario
            if jugador == max_j:
                if sim_puntos['puntuacion'] > mejor['puntuacion']:
                    mejor = sim_puntos #Remplazamos por la mejor puntuacion
            else:
                if sim_puntos['puntuacion'] < mejor['puntuacion']:
                    mejor = sim_puntos
        
        return mejor