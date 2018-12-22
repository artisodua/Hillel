# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все

# Дана произвольная строка
pstring = 'a !.How are you? Eh, ok. Low or Lower? Ohhh.'
# Дополнительная строка, для проверки того, что в строке всего одно слово,
# для проверки, раскоментировать и запустить
# pstring = 'How'

# Отсеиваем знаки припинания
def del_opunctuation_marks(string):
    plist = list(string)
    other_sint = ['!','.',',','?','-','_']
    for i in plist:
        if i in other_sint:
            plist.remove(i)
    return ''.join(plist)

pstring1 = del_opunctuation_marks(pstring)

# Находим первое слово в строке
def finde_first_char(string):
    list1 = string.split()
    if len(list1) > 1:
        for i in list1:
            if len(i) == 1 or i == ' ':
                continue
            else:
                print('First word in line = {}'.format(i))
                break
    else:
        print('Line hawe 1 word = {}'.format(list1))


print('Originsl line = {}'.format(pstring))
finde_first_char(pstring1)