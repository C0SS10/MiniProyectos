import re


def parse_input(cadena, gramatica, tabla_action, tabla_goto):
    pila = [0]  # Pila inicial con el estado 0
    indice = 0  # Índice para recorrer la cadena de entrada
    # Obtener tokens y lexemas de la cadena de entrada
    tokens_cadena = re.findall(
        r'[a-zA-Z_]\w*|\d+\.\d*|\d*\.?\d+|[\+\-\*/=()]|\;', cadena)
    lexemas = []  # Lista para almacenar los lexemas reconocidos
    tokens_lexemas = []  # Lista de pares (token, lexema)

    while True:
        estado = pila[-1]  # Estado en la cima de la pila

        if indice < len(tokens_cadena):
            # Símbolo actual de la cadena de entrada
            token = tokens_cadena[indice]
        else:
            token = "$"  # Símbolo de fin de entrada

        # Obtener acción de la tabla ACTION
        if re.match(r'[a-zA-Z_]\w*', token):
            token = 'id'
        elif re.match(r'[0-9]+(\.[0-9]+)?', token):
            token = 'num'
        action = tabla_action[estado].get(token)

        if action is None:
            print("Error en la cadena de entrada.")
            break

        if action.startswith("s"):  # Desplazamiento
            estado_siguiente = int(action[1:])
            pila.append(token)  # Insertar token en la pila
            pila.append(estado_siguiente)  # Insertar estado en la pila
            lexemas.append(tokens_cadena[indice])  # Agregar lexema reconocido
            # Agregar par (token, lexema)
            tokens_lexemas.append((token, tokens_cadena[indice]))
            indice += 1  # Avanzar al siguiente símbolo de entrada

        elif action.startswith("r"):  # Reducción
            indice_produccion = int(action[1:])  # Obtener índice de producción
            # Obtener la producción correspondiente
            produccion = gramatica[indice_produccion]

            # Símbolo no terminal de la producción
            no_terminal = produccion[0]

            # Extraer símbolos de la pila según la longitud de la producción
            for _ in range(2 * len(produccion[1])):
                pila.pop()

            estado_actual = pila[-1]
            estado_siguiente = tabla_goto[estado_actual].get(no_terminal)

            if estado_siguiente is None:
                break

            pila.append(no_terminal)  # Insertar símbolo no terminal en la pila
            pila.append(estado_siguiente)  # Insertar estado GOTO en la pila

        elif action == "accept":  # Aceptación
            break

    return pila, tokens_lexemas
