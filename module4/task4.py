alphabet = "abcdefg"

print(f"Копия строки: {alphabet[:]}")
print(f"Элементы строки в обратном порядке: {alphabet[::-1]}")
print(f"Каждый второй элемент строки (включая самый первый): {alphabet[::2]}")
print(f"Каждый второй элемент строки после первого: {alphabet[1::2]}")
print(f"Все элементы до второго: {alphabet[:1]}")
print(f"Все элементы, начиная с конца до предпоследнего: {alphabet[-1]}")
print(f"Все элементы в диапазоне индексов от 3 до 4 (не включая 4): {alphabet[3]}")
print(f"Последние три элемента строки: {alphabet[-3::]}")
print(f"Все элементы в диапазоне индексов от 3 до 4: {alphabet[3:5]}")
print(f"То же, что и в предыдущем пункте, но в обратном порядке: {alphabet[4:2:-1]}")