
def max_value(x):
    b = list(x)
    b.sort()
    b.reverse()
    return b[0], b[1], b[2]

def revers_ar(x):
    b = list(x)
    b.reverse()
    return b

def min_value(x):
    b = list(x)
    return min(b)

def unic_value(x):
    ar1 = list(x)
    ar2 = list()
    for i in ar1:
        if not i in ar2:
            ar2.append(i)
    return ar2

ar = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

print('Original array {} '.format(ar))
print('1. Max three value in array {}'.format(max_value(ar)))
print('2. Min value in array {}'.format(min_value(ar)))
print('3. Revers array {}'.format(revers_ar(ar)))
print('4. Unic array - {}'.format(unic_value(ar)))