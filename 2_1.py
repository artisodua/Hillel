from itertools import groupby
from operator import itemgetter
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}
    ]
# сортируем по значению 'age'
data.sort(key=lambda k: k["age"])
print('Sort_by_age:')
print(data)
print()

result = {}
for key, value in groupby(sorted(data, key=itemgetter("city")), key=itemgetter("city")):
    result.update({key: [{k: v for k, v in dictionary.items() if k != "city"} for dictionary in value]})
print('Regrouped_by_key_\'city\':')
print(result)