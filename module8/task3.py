site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def changeName(name: str, current_dict: dict):
    for key in current_dict.keys():
        if (type(current_dict[key]) is str):
            if ("{0}" in current_dict[key]): current_dict[key] = current_dict[key].format(name)
        elif (type(current_dict[key]) is dict): changeName(name, current_dict[key])

sites = []
sitesCount = int(input("Сколько сайтов: "))
for i in range(sitesCount):
    newSite = site_template.copy()
    changeName(input("Введите название продукта для нового сайта: "), newSite)
    sites.append(newSite)
    print("\n".join([str(s) for s in sites]))