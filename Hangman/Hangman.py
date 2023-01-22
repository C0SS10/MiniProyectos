import random
import string

def obtener_palabra():
    nombrearchivo = "Hangman/file.txt"
    contenido=[]
    with open(nombrearchivo) as dr:
        palabras = dr.readlines()
        for linea in palabras:
            contenido.append(linea.strip('\n'))
    
    palabra = random.choice(contenido)
    while 'Ã³' in palabra or 'Ã±' in palabra:
        #Si la palabra contiene carácteres que no quiero sigue buscando una palabra valida
        palabra = random.choice(contenido)

    return palabra.upper() #Retorna la palabra en mayusculas

def ahorcar():
    palabra = obtener_palabra()
    letras = set(palabra) #Divide las letras de la palabra
    alfabeto = set(string.ascii_uppercase) #Obtenemos las letras del alfabeto
    alfabeto.update('Ñ','Á','É','Í','Ó','Ú')
    letras_usadas = set()
    oportunidades = 4

    while len(letras) > 0 and oportunidades > 0:
        #Letras usadas
        # ' '.join(['a','b', 'cd']) ---> 'a b cd'
        print(f'\nTienes {oportunidades} oportunidades\nHas usado las siguientes letras: ',' '.join(letras_usadas))

        #Dónde están las letras usadas
        #En la posición de la lista, se crea 'letter'
        #Si la letra está entre las letras usadas se revela
        #Las dejas letras permanecen ocultas con un '-' si no son reveladas por el jugador
        lista_letra = [letter if letter in letras_usadas else '-' for letter in palabra]
        print('La palabra es: ',' '.join(lista_letra))

        letra_jugador = input('Ingrese una letra: ').upper()
        #Si la letra del jugador es diferentes a las que usó anteriormente y está en el alfabeto
        if letra_jugador in alfabeto - letras_usadas:
            #Se agrega a la lista de letras usada la letra ingresada por el jugador
            letras_usadas.add(letra_jugador)
            if letra_jugador in letras:
                letras.remove(letra_jugador)
            else:
                oportunidades -= 1
            
        elif letra_jugador in letras_usadas:
            print(f'La letra {letra_jugador} ya la has utilizado')

        else:
            print(f'{letra_jugador} ESO NO ES UN CARÁCTER')

    if oportunidades == 0:
        print(f'La palabra era: {palabra} , has PERDIDO')
    else:
        print(f'La palabra es: {palabra} , has GANADO')