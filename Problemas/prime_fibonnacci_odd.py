def is_Prime(n):
    if n <= 1:
        return f'{n} no es primo,'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f'{n} no es primo,'
    return f'{n} es primo,'


def is_Fibonacci(n):
    r = ''
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        r += ' fibonacci'
        r = ''.join(is_Odd_Even(n, r))
        return r
    else:
        r += ' no es fibonacci'
        r = ''.join(is_Odd_Even(n, r))
        return r


def is_Odd_Even(n, r):
    if n % 2 == 0:
        r += f' y es par'
        return r
    else:
        r += f' y es impar'
        return r


nums = [1, 3, 89, 55, 4, 233, 11, 33, 8]
for i in nums:
    result = is_Prime(i)
    result += ''+is_Fibonacci(i)
    print(result)
