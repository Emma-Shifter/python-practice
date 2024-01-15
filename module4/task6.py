listsCount = int(input("Введите количество списков в списке: "))
listElemCount = int(input("Введите количество элементов во вложенном списке: "))

res = [
    [(list_index + 1) + listsCount * element_in_list_index for element_in_list_index in range(listElemCount)]
    for list_index in range(listsCount)
]

print(res)