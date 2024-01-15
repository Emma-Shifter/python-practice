shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], 
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
optimized_shop = {}
for item in shop:
    if (item[0] in optimized_shop):
        optimized_shop[item[0]].append(item[1])
    else: optimized_shop[item[0]] = [item[1]]

detail = input("Название детали: ")
if (detail in optimized_shop):
    print(f"Количество деталей: {len(optimized_shop[detail])}\nОбщая стоимость: {sum(optimized_shop[detail])}")
else:
    print("Количество деталей: 0\nОбщая стоимость: 0")