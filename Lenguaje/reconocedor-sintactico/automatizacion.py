import re

tabla = {
    'E': {
        'id': 'TF',
        'num': 'TF',
        '(': 'TF',
    },
    'F': {
        '+': '+TF',
        '-': '-TF',
        ')': 'λ',
        '$': 'λ'
    },
    'T': {
        '(': 'GH',
        'id': 'GH',
        'num': 'GH',
    },
    'H': {
        '*': '*GH',
        '/': '/GH',
        '+': 'λ',
        '-': 'λ',
        ')': 'λ',
        '$': 'λ'
    },
    'G': {
        '(': '(E)',
        'id': ['id'],
        'num': ['num']
    }
}


def auto(tokens):
    # Inicialización de la pila, el índice y el miratabla
    pila = ['$', 'E']
    i = 0
    t = ''
    listaTokens = re.findall(r'\w+|\*|\-|\+|\/|\(|\)|\=',tokens)
    miratabla = listaTokens[i]

    while len(pila) > 0:
        # Obtenemos el tope de la pila
        tope = pila[-1]
        print(pila)
        if tope == miratabla:
            # Si el tope de la pila es igual al miratabla, avanzamos en la entrada
            # y actualizamos el miratabla
            pila.pop()
            i += 1
            if i < len(listaTokens):
                miratabla = listaTokens[i]
            else:
                miratabla = '$'
        elif tope.isupper() and tope in tabla and miratabla in tabla[tope]:
            # Si el tope de la pila es un no terminal y hay una entrada en la tabla para
            # ese no terminal y el miratabla actual, aplicamos la producción correspondiente
            produccion = tabla[tope][miratabla]
            if produccion != 'λ':
                # Si la producción no es la cadena vacía, desapilamos el no terminal y
                # apilamos los símbolos de la producción en orden inverso
                pila.pop()
                for simbolo in reversed(produccion):
                    pila.append(simbolo)
            else:
                # Si la producción es la cadena vacía, simplemente desapilamos el no terminal
                pila.pop()
        else:
            # Si no se cumple ninguna de las dos condiciones anteriores, es un error de
            # análisis sintáctico
            return False
    # Si llegamos al final y la pila está vacía, la cadena fue aceptada
    return True


# Pruebas
print(auto('num+id*num'))  # True
print()
print(auto('id*(id+num*id)'))  # True
print()
print(auto('num*/id')) # False