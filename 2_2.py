# 2) У вас есть последовательность строк.
# Необходимо определить наиболее часто встречающуюся строку в последовательности.

new = ['bla', 'bla', 'hello', 'hello', 'bla', 'igogo', 'aloha','bla','bla','bla','bla','hello','hello']
# заливаем в dict строки с ключем - их количество в последовательности
def max_line(new):
    dict = {}
    for i in range(len(new)):
         line = new[i]
         x = 0
         for j in new:
             if j == line:
                x += 1
                dict[line] = x
             else:
                 continue
    return dict
# присваиваем переменной max_item строку которая чаще всего встречалась в последовательности
max_item = max(max_line(new), key=max_line(new).get)
print('Наиболее часто встречающуюся строку в последовательности - {}'.format(max_item))