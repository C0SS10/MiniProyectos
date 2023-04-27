"""  * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a") """


def toLeet(s: str):
    table = {
        'A': '4', 'B': 'l3', 'C': '[', 'D': ')',
        'E': '3', 'F': '|=', 'G': '&', 'H': '#',
        'I': '1', 'J': ',_l', 'K': '>|', 'L': '1',
        'M': '/\/\ ', 'N': '^/', 'O': '0', 'P': '|*',
        'Q': '(_,)', 'R': 'l2', 'S': '5', 'T': '7',
        'U': '(_)', 'V': '\/', 'W': '\/', 'X': '><',
        'Y': 'j', 'Z': '2'
    }
    s = s.upper()
    translated = str.maketrans(table)
    print(s.translate(translated))


toLeet('La vida en la presurisada evidencia del ser')
