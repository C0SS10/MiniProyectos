import secrets
import string
import random

"""  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos) """

symbols = string.ascii_lowercase + string.ascii_uppercase \
    + string.digits + string.punctuation


def make_password():
    password = ''
    lenght = random.randint(8, 16)
    for i in range(lenght):
        password += ''.join(secrets.choice(symbols))
    return password


new_password = make_password()
print(f'The password is: {new_password}')
