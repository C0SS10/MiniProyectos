import random

def jugar():
    jugador = input(f"Elige: 'r' para roca, 'p' para papel, 't' para tijeras\n")
    computador = random.choice(['r','p','t'])
    if jugador == computador:
        return print(f'Jugador: {jugador} vs {computador} :arodatupmoC \n Es un EMPATE')
    if gano(jugador, computador):
        return print(f'Jugador: {jugador} vs {computador} :arodatupmoC \n Has GANADO')

    return print(f'Jugador: {jugador} vs {computador} :arodatupmoC \n Has PERDIDO')

def gano(j,c):
    #r > t, t > p, p > r
    if (j == 'r' and c == 't') or (j == 'p' and c == 'r') or (j== 't' and c == 'p'):
        return True
