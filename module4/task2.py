n = int(input("Введите длину списка: "))
res = [1 if (i % 2 == 0) else i % 5 for i in range(n)]
print(f"Результат: {res}")