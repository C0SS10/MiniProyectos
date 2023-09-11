import tkinter as tk
from tkinter import scrolledtext
import analizador as reconocer

TABLA_ACTION = {
    0: {'id': 's2', 'A': 1},
    1: {'$': 'accept'},
    2: {'=': 's3'},
    3: {'id': 's7', 'num': 's8', '(': 's9', 'E': 4, 'T': 5, 'F': 6},
    4: {';': 's10', '+': 's11', '-': 's12'},
    5: {';': 'r3', '+': 'r3', '-': 'r3', '*': 's13', '/': 's14', ')': 'r3'},
    6: {';': 'r6', '+': 'r6', '-': 'r6', '*': 'r6', '/': 'r6', ')': 'r6'},
    7: {';': 'r7', '+': 'r7', '-': 'r7', '*': 'r7', '/': 'r7', ')': 'r7'},
    8: {';': 'r8', '+': 'r8', '-': 'r8', '*': 'r8', '/': 'r8', ')': 'r8'},
    9: {'id': 's7', 'num': 's8', '(': 's9', 'E': 15, 'T': 5, 'F': 6},
    10: {'$': 'r0'},
    11: {'id': 's7', 'num': 's8', '(': 's9', 'T': 16, 'F': 6},
    12: {'id': 's7', 'num': 's8', '(': 's9', 'T': 17, 'F': 6},
    13: {'id': 's7', 'num': 's8', '(': 's9', 'F': 18},
    14: {'id': 's7', 'num': 's8', '(': 's9', 'F': 19},
    15: {'+': 's11', '-': 's12', ')': 's20'},
    16: {';': 'r1', '+': 'r1', '-': 'r1', '*': 's13', '/': 's14', ')': 'r1'},
    17: {';': 'r2', '+': 'r2', '-': 'r2', '*': 's13', '/': 's14', ')': 'r2'},
    18: {';': 'r4', '+': 'r4', '-': 'r4', '*': 'r4', '/': 'r4', ')': 'r4'},
    19: {';': 'r5', '+': 'r5', '-': 'r5', '*': 'r5', '/': 'r5', ')': 'r5'},
    20: {';': 'r9', '+': 'r9', '-': 'r9', '*': 'r9', '/': 'r9', ')': 'r9'}
}

GRAMATICA = [
    ("A", ["id", "=", "E", ";"]),
    ("E", ["E", "+", "T"]),
    ("E", ["E", "-", "T"]),
    ("E", ["T"]),
    ("T", ["T", "*", "F"]),
    ("T", ["T", "/", "F"]),
    ("T", ["F"]),
    ("F", ["id"]),
    ("F", ["num"]),
    ("F", ["(", "E", ")"])
]

TABLA_GOTO = {0: {'A': 1}, 3: {'E': 4, 'T': 5, 'F': 6}, 9: {'E': 15, 'T': 5, 'F': 6}, 11: {
    'T': 16, 'F': 6}, 12: {'T': 17, 'F': 6}, 13: {'F': 18}, 14: {'F': 19}}


def analizar_cadena():
    cadena = entrada.get()

    # Realizar el análisis de la cadena y obtener los pares token_lexema
    pila, tokens_lexemas = reconocer.parse_input(
        cadena, GRAMATICA, TABLA_ACTION, TABLA_GOTO)

    # Crear una cadena con todos los pares token_lexema
    resultados = ""
    for token, lexema in tokens_lexemas:
        resultados += f"Token: {token}, Lexema: {lexema}\n"

    # Verificar si el análisis fue correcto
    analisis_correcto = "Cadena reconocida correctamente." if pila[-1] == 1 else "Error en la cadena de entrada."

    # Actualizar el texto del área de texto
    texto.delete(1.0, tk.END)  # Borrar el contenido anterior
    texto.insert(tk.END, resultados + analisis_correcto)


# Crear la ventana
ventana = tk.Tk()
ventana.title("Análisis de Cadenas")
ventana.geometry("800x500")
fuente = ("Cascadia Code", 14)
ventana.configure(bg="#1F497D")

# Crear el campo de entrada
entrada = tk.Entry(ventana, font=fuente)
# Agregar espacio vertical entre el campo de entrada y el botón
entrada.pack(pady=10)

# Crear el botón de análisis
boton_analizar = tk.Button(ventana, text="Analizar",
                           font=fuente, command=analizar_cadena)
# Agregar espacio vertical entre el botón y la etiqueta
boton_analizar.pack(pady=10)

# Crear el área de texto desplazable
texto = scrolledtext.ScrolledText(
    ventana, width=50, height=15, wrap=tk.WORD, font=fuente)
texto.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Centrar el área de texto

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()

# Hecho por Esteban Cossio Gonzalez
# TIP: 1020495759
