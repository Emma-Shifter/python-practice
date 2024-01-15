vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}

input = input("Введите текст: ")
vowels_in_input = [letter for letter in input if letter in vowels]

print(f"Список гласных букв: {vowels_in_input}\nДлина списка: {len(vowels_in_input)}")