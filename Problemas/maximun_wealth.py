def maximumWealth(accounts):
    maxDinero = 0
    for i in range(len(accounts)):
        #   suma cada fila ya que representa el dinero de cada cliente
        dineroActual = sum(accounts[i])
        #   Si el dineroActual es mayor que el dinero máximo actual actualiza
        #   si por ejemplo dinero actual es 16 y maxDinero es 78 no actualiza
        maxDinero = max(dineroActual, maxDinero)
    return maxDinero


accounts = [[15, 20, 3], [3, 2, 8], [10, 4, 1]]
print(maximumWealth(accounts))
