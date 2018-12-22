# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n.
# Если n за границами массива, тогда вернуть -1.

ar = [1, 2, 3, 4, 5, 6]
n = 7

def some_function(ar, n):
    if n > len(ar) or n < 0:
        print('-1')
    else:
        x = ar[n]**n
        return x

print(some_function(ar, n))