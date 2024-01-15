default = [1, 2, 3, 4, 5]
offset = int(input("Сдвиг: "))
print(f"Изначальный список: {default}")
print(f"Сдвинутый список: {[default[i % len(default)] for i in range(-offset, len(default) - offset)]}")