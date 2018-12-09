
soglas = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
          'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
glas = 'a'

text = 'Less than a minute later, she walked out and grabbed a gun from'

text_to_list = list(text)
new_streeng = []

for i in text_to_list:
    if i not in soglas:
        new_streeng.append(str(i))
    else: new_streeng.append(glas)

print(''.join(new_streeng))