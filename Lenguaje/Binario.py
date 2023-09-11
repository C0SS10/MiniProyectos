def convertirBinario():
    cadena = str(input('Ingrese cadena: '))
    cadena_bin = ' '.join(format(c,'b') for c in bytearray(cadena,'utf-8'))
    return cadena_bin