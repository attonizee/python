import pickle
import json


my_favourite_group = {
    'name': 'Г.М.О',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': '2016'}, 
    {'name': 'Шапито', 'year': '2014'}]
}


group_byte = pickle.dumps(my_favourite_group)
print(group_byte)
group_json = json.dumps(my_favourite_group)
print(group_json)


with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)


print('saved group.pickle')


with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)


print('saved group.json')