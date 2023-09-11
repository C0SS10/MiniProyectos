#   Elaborar un programa que nos permita simular el comportamiento de un autómata finito 
#   que reconozca constantes numéricas.

def reconocerNumericos(entrada):
    estado = 0
    signo = 1
    for char in entrada:
        if estado == 0:
            if char == '-':
                signo = -1
                estado = 1
            elif char == '+':
                estado = 1
            elif char.isdigit():
                estado = 2
            else:
                return False
        elif estado == 1:
            if char.isdigit():
                estado = 2
            else:
                return False
        elif estado == 2:
            if char.isdigit():
                estado = 2
            elif char == '.':
                estado = 3
            elif char in ['e', 'E']:
                estado = 5
            else:
                return True
        elif estado == 3:
            if char.isdigit():
                estado = 4
            else:
                return False
        elif estado == 4:
            if char.isdigit():
                estado = 4
            elif char in ['e', 'E']:
                estado = 5
            else:
                return True
        elif estado == 5:
            if char in ['+', '-']:
                estado = 6
            elif char.isdigit():
                estado = 7
            else:
                return False
        elif estado == 6:
            if char.isdigit():
                estado = 7
            else:
                return False
        elif estado == 7:
            if char.isdigit():
                estado = 7
            else:
                return True
    if estado in [2, 4, 7]:
        return True
    return False