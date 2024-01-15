special_simbols = {"@", "№", "$", "%", "^", "&", "*", "(", ")"}
file = input("Название файла: ")
if (file[0] in special_simbols): print("Ошибка: название начинается недопустимым символом")
elif (file.endswith(".txt") or file.endswith(".docx")): print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else: print("Файл назван верно.")