import pprint
data = [
    {'name': 'Viktor',  'city': 'Kiev', 'age': 30},
    {'name': 'Maksim',  'city': 'Dnepr','age': 20},
    {'name': 'Vladimir','city': 'Lviv', 'age': 32},
    {'name': 'Andrey',  'city': 'Kiev', 'age': 34},
    {'name': 'Artem',   'city': 'Dnepr','age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}
]

data.sort(key=lambda y: y['age'])
print('Sort_by_age:')
print(data)
print()

new_data = {}
for i in range(len(data)):
    city_value = data[i]['city']
    city_key = data[i].pop('city')

    if city_value in new_data.keys():
        new_data[city_value].append(data[i])
    else:
        new_data[city_value] = [data[i]]


print('Regrouped_by_key_\'city\':')
print(new_data)
print()
# Красивый вывод на экран
pprint.pprint(new_data)