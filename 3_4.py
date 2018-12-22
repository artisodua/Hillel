# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.
char = 'How are yoU'

def change_char(text):
    plist = list(text)
    first = plist[0]
    last = plist[-1]
    plist.pop()
    plist.reverse()
    plist.pop()
    plist.reverse()
    plist.insert(0,last)
    plist.extend(first)
    return ''.join(plist)

print('Исходная строка - {}'.format(char))
print('Поменяны местами первая и последняя буква в строке - {}'.format(change_char(char)))