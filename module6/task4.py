import collections

input = input("Введите текст: ")
origin = collections.Counter(input)
inverted = {}

for key in origin.keys():
    if (origin[key] in inverted): inverted[origin[key]].append(key)
    else: inverted[origin[key]] = [key]

print(f"Инвертированный словарь частот: {inverted}")