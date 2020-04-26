import pickle
import json

with open('group.pickle', 'rb') as f:
    my_favorite_group = pickle.load(f)

print(my_favorite_group)

with open('group.json', 'r', encoding='utf-8') as f:
    my_favorite_group = json.load(f)

print(my_favorite_group)