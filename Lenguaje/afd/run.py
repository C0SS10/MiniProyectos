import Ceros_Unos as C
import Lenguaje as Le

if __name__ == '__main__':
    # Lenguaje
    L = Le.generarLenguaje()
    for i in range(len(L)):
        print(f'¿La secuencia {L[i]} es valida?: {C.reconocerSecuencia(L[i])}')

        ceros = L[i].count('0')
        unos = L[i].count('1')
        print(f'\nLa cantidad de ceros (0) es: {ceros}')
        print(f'La cantidad de unos (1) es: {unos}')
        print('\n==============================================================\n')