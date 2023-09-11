class AutomataPila:
    def __init__(self):
        self.alfabeto = {'a', 'b', 'c'}
        self.alfabeto_pila = {'B', 'Z'}
        self.estados = {'q0', 'q1', 'q2'}
        self.estado_inicial = 'q0'
        self.estados_aceptacion = {'q2'}
        self.funcion_transicion = {
            ('q0', 'a', 'Z'): ('q1', 'Z'),
            ('q1', 'b', 'Z'): ('q1', 'B'),
            ('q1', 'b', 'B'): ('q1', 'Z'),
            ('q1', 'c', 'Z'): ('q2', 'Z'),
            ('q1', 'c', 'B'): ('q2', 'Z'),
            ('q2', ' ', 'Z'): ('q2', ' '),
        }

    def procesar_cadena(self, cadena):
        pila = []
        pila.append('Z')
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False
            if (estado_actual, simbolo, pila[-1]) in self.funcion_transicion:
                nuevo_estado, nuevo_simbolo_pila = self.funcion_transicion[(estado_actual, simbolo, pila[-1])]
                if nuevo_simbolo_pila == ' ':
                    pila.pop()
                if nuevo_simbolo_pila == 'Z':
                    pila.extend(list(nuevo_simbolo_pila)[::-1])
                estado_actual = nuevo_estado
            else:
                return False
        if estado_actual in self.estados_aceptacion and pila[-1] == 'Z':
            return True
        else:
            return False

automata = AutomataPila()
cadenas = ['abbc', 'aabc', 'aabbc', 'ac', 'abcabcabc']

for cadena in cadenas:
    if automata.procesar_cadena(cadena):
        print(f'La cadena {cadena} ES aceptada por el autómata.')
    else:
        print(f'La cadena {cadena} NO es aceptada por el autómata.')