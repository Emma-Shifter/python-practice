site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def getValue(find_key: str, pass_obj: dict, left_deep) -> object:
    if (left_deep == 0): return None
    if (find_key in pass_obj): return pass_obj[find_key]
    else:
        for obj_key in pass_obj.keys():
            if (type(pass_obj[obj_key]) is dict):
                returned_value = getValue(find_key, pass_obj[obj_key], maxDeep - 1)
                if (returned_value is not None): return returned_value
    return None


key = input("Введите искомый ключ: ")
hasDeep = True if input("Хотите ввести максимальную глубину? Y/N: ").lower() == "y" else False
maxDeep = int(input("Введите максимальную глубину: ")) if hasDeep else float("inf")
print(f"Значение ключа: {getValue(key, site, maxDeep)}")