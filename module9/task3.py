import os
def getCataogInfo(path: str) -> (int, int, int):
    totalCatalogWeight = 0
    catalogsCount = 0
    filesCount = 0
    for directory in os.listdir(path):
        if (os.path.isdir(os.path.join(path, directory))):
            info = getCataogInfo(os.path.join(path, directory))
            totalCatalogWeight += info[0]
            catalogsCount += info[1] + 1
            filesCount += info[2]
        elif (os.path.isfile(os.path.join(path, directory))):
            totalCatalogWeight += os.path.getsize(os.path.join(path, directory))
            filesCount += 1
    return totalCatalogWeight, catalogsCount, filesCount

catalogInfo = getCataogInfo(input("Введите путь: "))
print(f"Размер каталога (в Кбайтах): {catalogInfo[0] / 1024}\n"
      f"Количество подкаталогов: {catalogInfo[1]}\n"
      f"Количество файлов: {catalogInfo[2]}")