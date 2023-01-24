def solucion():
    movimiento = [
        #Derecha
        [1,0],
        #Arriba
        [0,1],
        #Izquierda
        [-1,0],
        #Abajo
        [0,-1]
    ]

    while(True):
        try:
            #   El input que ingrese el usuario deberá ser: '2 8 1 1'
            n, c, x, y = list(map(int, input('Ingrese los valores (n,c,x,y) respectivamente: ').split()))

        except ValueError:
            # No es un número
            print("Input invalido")
            continue
        
        #   Si todos los valores son iguales a 0 0 0 0 sale del ciclo
        if n == c == x == y == 0:
            break
        
        #   creación del mundo donde la hormiga camina
        mundo = [['.' for j in range(n)] for i in range(n)]

        #   es un número natural que se codificara en binario
        nro_codificado = n * n

        #   Llenando el mundo con los colores que nos dicen 'R' y 'B'
        for filas in range(n):
            for columnas in range(n):
                #   Al valor natural del nro codificado le restaremos 1. Tomamos '2 8 1 1'
                #   a ese nuevo nro codificado, en este caso 2*2 = 4 - 1 = 3
                nro_codificado -= 1
                #   movemos a la izquierda el bit '1' 3 veces -> 1000, en natural sería 8
                #   luego conjugamos 8 en binario con el valor de c en este caso 8
                #   como resultado nos da de nuevo 8, si conjugamos el mismo valor de c en binario:
                if (1 << nro_codificado) & c:
                    #   Si cumple la anterior operación, coloreamos la casilla acutal de color rojo
                    mundo[filas][columnas] = 'R'
                else:
                    #   Si no cumple la anterior operación, coloreamos la casilla actual de color azul
                    mundo[filas][columnas] = 'B'
        
        #   inicialmente restamos 1 punto a cada coordenada
        x -= 1
        y -= 1
        giro = 0
        
        #   hacemos el seguimiento de si pasa por las coordenadas n,n [True]
        #   si nunca pasa por el punto n,n [False] o se muere la hormiga
        pasa = False

        while(True):
            #   Condiciones para controlar si la hormiga se sale del mundo
            if y < 0 or y >= n or x < 0 or x >= n:
                #   la hormiga muere
                break
            
            #   Si la hormiga llega a la celda n,n desde el punto inicial
            if x == y == n - 1:
                pasa = True
                break
            
            if mundo[y][x] == 'R':
                #   Si la hormiga llega a una casilla de color Roja la cambia a Azul
                mundo[y][x] = 'B'
                #   Luego recalcula el giro que va a hacer, esto es actualizar las coordenadas
                giro = (giro + 3) % 4
                y += movimiento[giro][0]
                x += movimiento[giro][1]
            else:
                #   Si la hormiga llega a una casilla de color Azul la cambia a Roja
                mundo[y][x] = 'R'
                #   Luego recalcula el giro que va a hacer, esto es actualizar las coordenadas
                giro = (giro + 1) % 4
                y += movimiento[giro][0]
                x += movimiento[giro][1]
        
        if pasa:
            print('Yes')
        
        else:
            print('Kaputt!')