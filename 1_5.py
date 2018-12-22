
dict_one = {'a':1, 'b':2, 'c':3, 'd':4}
dict_two = {'a':6, 'b':7, 'z':8, 'x':2}
newList = []
for i in dict_one:
    if i in dict_two:
        newList.append(i)

print('Similar Keys in to dict - {}'.format(newList))