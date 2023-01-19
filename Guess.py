import random

def adivinar(x):
    adivinado = "null"
    numero_random = random.randint(0,x)

    while adivinado != numero_random:
        adivinado = int(input(f'Adivina el número (0,{x}): '))
        if adivinado < numero_random:
            print(f'El {adivinado} es menor')
        elif adivinado > numero_random:
            print(f'El {adivinado} es mayor')
    
    print(f'LO ADIVINASTE, EL NÚMERO ES: {numero_random}')

def adivinar_pc(x):
    inf = 0
    sup = x
    respuesta = ''

    while respuesta != 'c':
        if inf != sup:
            num_random = random.randint(inf,sup)
        else:
            num_random = inf
        respuesta = input(f'El {num_random} es mayor [H], El número es menor [L],\
             El número es correcto [C] \n')
        if respuesta == 'h':
            sup = num_random - 1
        elif respuesta == 'l':
            inf = num_random + 1

    print(f'LA COMPUTADORA ADIVINÓ, {num_random}, es el número correcto')