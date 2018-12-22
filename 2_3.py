# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

char = '123405023501'

def composition_char(text):
    list1 = list(text)
    composition = True
    for i in list1:
        if i == '0':
            continue
        else:
            composition *= int(i)
    return composition

composition = composition_char(char)

print('Произведение всех цифр из числа {} не учитывая нули = {}'.format(char, composition))