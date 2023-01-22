def leer_txt(direccion):
    with open(direccion,'r') as f:
        #   Leyendo el texto y guardandolo como un string
        texto = f.read()
        #   Los espacios exagerados se convierten en uno solo
        #   'Este   es  el   texto' -> 'Este es el texto'
        texto = ' '.join(texto.split())
        texto = texto.lower() # minisculas
