"""  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.    """

points = {0: 'Love',
          1: '15',
          2: '30',
          3: '40',
          4: 'Deuce',
          5: 'Adventage',
          6: 'Winner'}


def match_Result(sequence):
    scoreP1 = 0
    scoreP2 = 0
    i = 0
    while i != len(sequence):
        P1 = points[scoreP1]
        P2 = points[scoreP2]

        if sequence[i] == 'P1':
            scoreP1 += 1
            P1 = points[scoreP1]
            if scoreP1 == scoreP2 == 3:
                print(f'{points[4]}')
            elif scoreP1 >= 4:
                print(f'{points[scoreP1+1]} P1')
            else:
                print(f'{P1} - {P2}')

        elif sequence[i] == 'P2':
            scoreP2 += 1
            P2 = points[scoreP2]
            if scoreP1 == scoreP2 == 3:
                print(f'{points[4]}')
            elif scoreP2 >= 4:
                print(f'{points[scoreP2+1]} P2')
            else:
                print(f'{P1} - {P2}')

        i += 1


s = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
match_Result(s)
