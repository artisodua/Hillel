# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
text = 'HHow are you? Eh, ok. Low or Lower? Ohhh.'

def upper_word(string):
    list1 = list(map(chr, range(ord('A'), ord('Z') + 1)))
    list2 = []
    for i in list(string):
        if i in list1:
            list2.append(i)
    return list2

print(''.join(upper_word(text)))