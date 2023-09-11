import tkinter as tk
from Analizador import analizar

# Función para el botón 'analizar'
def analizarEntrada():
    # Obteniendo la entrada de la barra de entradas
    entrada = barraEntrada.get()
    # Analiza lexicamente la entrada
    tokens = analizar(entrada)
    barraEntrada.delete(0, tk.END) #Refresca la barra de entradas
    # Muestra el resultado en la caja de resultado
    resultado = f"Su entrada: {entrada}\n\n"
    for token in tokens:
        resultado += f"{token[0]}: {token[1]}\n"
    
    labelResultado.configure(state='normal')
    labelResultado.delete('0.8', tk.END)
    labelResultado.insert(tk.END, resultado)
    labelResultado.configure(state='disabled')

# Crea una ventana principal
ventana = tk.Tk()
ventana.geometry("400x500")
ventana.configure(bg="#00843D")
ventana.title("Analizador léxico")
icono_16 = tk.PhotoImage(file='analizador_lexico/cal-16.png')
icono_32 = tk.PhotoImage(file='analizador_lexico/cal-32.png')
ventana.iconphoto(True, icono_16, icono_32)

tamañoFuente = 14

# Creando la barra de entradas
barraEntrada = tk.Entry(ventana, font=("Cascadia Code", tamañoFuente))
barraEntrada.pack(pady=10)

# Creando el boton 'analizar'
btnAnalizar = tk.Button(ventana, text="Analizar", font=("Cascadia Code", tamañoFuente), command=analizarEntrada)
btnAnalizar.pack(pady=10)

# Crando una caja que contenga el resultado del analisis and la barra de desplazamiento
cajaResultado = tk.Frame(ventana)
cajaResultado.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Creando el texto de resultado
labelResultado = tk.Text(cajaResultado, font=("Cascadia Code", tamañoFuente), wrap=tk.WORD)
labelResultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
labelResultado.configure(state='normal', bg='#005151', fg='white')

# Creando la barra de desplazamiento para el resultado del analisis
barraDesplaza = tk.Scrollbar(cajaResultado)
barraDesplaza.pack(side=tk.RIGHT, fill=tk.Y)

# Configurando la barra desplazadora.
labelResultado.config(yscrollcommand=barraDesplaza.set)
barraDesplaza.config(command=labelResultado.yview)

ventana.mainloop()

#[(4+9)/5*2]
#1*5+(2-43)/5+1+[48-9+(21*1)]