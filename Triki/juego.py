import time
from Triki.jugador import JugadorHumano, JugadorComputadora, ComputadoraGenio
#Creamos una clase Triki [Super clase]. ¡Esto es lo segundo que se debe hacer!

class Triki:
    def __init__(self):
        #Se usa una lista para representar el tablero 3x3
        self.tablero = [' ' for _ in range(9)]
        self.actual_ganador = None

    def imprimir_tablero(self):
        #Hay tres grupos de casillas (La fila 1, 2 y 3) [| | | |]
        for fila in [self.tablero[i*3:(i+1)*3]for i in range(3)]:
            print('| '+ ' | '.join(fila) + ' |')

    #¡METODO ESTÁTICO! No tenemos que pasarle un 'self'
    @staticmethod
    def imprimir_tablero_num():
        #Tenemos que saber que número le corresponde a cada lugar del tablero; [| 0 | 1 | 2 |]
        #j*3 es para las columnas y (j+1)*3 es para las filas (2+1)*3= 9
        #j solo obtiene números de 0 a 2 (range(3)) EMPIEZA EN 0-8
        tablero_numerico = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for fila in tablero_numerico:
            print('| '+ ' | '.join(fila)+' |')

    #Debemos saber que espacios están disponibles para hacer un movimiento
    def mvto_disponible(self):
        #Va a retornar una lista []
        #mvtos_posibles = []
        #for (i,lugar) in enumerate(self.tablero):
            #[(0,'x'), (1,'x'), (2,'o')] es un mapa de cordenadas con el lugar y el simbolo
            #if lugar == ' ':
                #mvtos_posibles.append(i)

        #return mvtos_posibles
        return [i for i, lugar in enumerate(self.tablero) if lugar == ' ']

    def cuadros_vacios(self):
        return ' ' in self.tablero

    def numero_cuadros_vacios(self):
        #Para saber los cuadros disponibles o vacios return {len(self.mvto_disponible())}
        return self.tablero.count(' ')

    def hacer_mvto(self,cuadro,sym):
        #Si el movimiento es valido a ese cuadro se le asigna el simbolo
        #Si es un movimiento valido retornamos true si no, retornamos false
        if self.tablero[cuadro] == ' ':
            self.tablero[cuadro] = sym
            if self.ganador(cuadro,sym):
                self.actual_ganador = sym
            return True

        return False

    def ganador(self,cuadro,sym):
        #El ganador es el que primero consiga 3 simbolos haciendo una línea recta
        #Debemos identificar las filas, columnas y diagonales
        fila_ind = cuadro // 3
        fila = self.tablero[fila_ind*3: (fila_ind+1)*3]
        #Si una fila tiene los mismos simbolos 3 tres vece 
        if all([lugar == sym for lugar in fila]):
            return True
        
        #Revisando columnas
        col_ind = cuadro % 3
        #En este caso utilizamos la iteración de columnas (j+1)*3 cambiando '1' por 'i'
        col = [self.tablero[col_ind+i*3] for i in range(3)]
        if all([lugar == sym for lugar in col]):
            return True
        
        #Revisando diagonales, las cuales son: 0,2,4,6,8 (números pares)
        if cuadro % 2 == 0:
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]]
            if all([lugar == sym for lugar in diagonal1]):
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]]
            if all([lugar == sym for lugar in diagonal2]):
                return True
        
        #Si no tenemos ganador
        return False

def jugar(imprimir_juego = True):
    juego = Triki()

    jugador_x = JugadorHumano('X')
    jugador_o = ComputadoraGenio('O')

    if imprimir_juego:
        juego.imprimir_tablero_num()

    sym = 'X' #sym inicial
    #Debemos iterar hasta que no hayan cuadros (lugares) disponibles
    while juego.cuadros_vacios():
        if sym == 'O':
            cuadro = jugador_o.obtener_mvto(juego)
        else:
            cuadro = jugador_x.obtener_mvto(juego)
    
        #Función para hacer un movimiento
        if juego.hacer_mvto(cuadro,sym):
            if imprimir_juego:
                print(sym + f' Haz hecho un movimiento al cuadro #{cuadro}')
                juego.imprimir_tablero()
                print('')
            
            #Si hay un ganador retornamos el simbolo.
            if juego.actual_ganador:
                if imprimir_juego:
                    print(sym + ' ¡GANO! ')
                return sym

        #Para alternar simbolo o turno
        sym = 'O' if sym == 'X' else 'X'
    
    #Pequeño descanso 
    #if imprimir_juego: Quitar el if si quiero jugar
    time.sleep(0.8)

    if imprimir_juego:
        print('Es un empate')

