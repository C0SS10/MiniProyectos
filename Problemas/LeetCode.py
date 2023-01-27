#   Sumar la lista (Running Sum)
def runningSum(nums):
    #   [0+1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

def maximumWealth(accounts):
    maxDinero = 0
    for i in range(len(accounts)):
        #   suma cada fila ya que representa el dinero de cada cliente
        dineroActual = sum(accounts[i])
        #   Si el dineroActual es mayor que el dinero máximo actual actualiza
        #   si por ejemplo dinero actual es 16 y maxDinero es 78 no actualiza
        maxDinero = max(dineroActual,maxDinero)
    return maxDinero

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    accounts = [[15,20,3],[3,2,8],[10,4,1]]
    print(runningSum(nums))
    print(maximumWealth(accounts))