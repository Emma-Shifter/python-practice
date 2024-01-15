def getLowercase(word: str) -> str:
    return word.lower()

def getCapitalize(word: str) -> str:
    return word.capitalize()

synonyms = {}
for i in range(int(input("Введите количество пар слов: "))):
    first_word, second_word = map(getLowercase, input(f"{i + 1} пара: ").split(" - "))
    if (first_word in synonyms): synonyms[first_word].append(second_word)
    else: synonyms[first_word] = [second_word]
    if (second_word in synonyms): synonyms[second_word].append(first_word)
    else: synonyms[second_word] = [first_word]


while (input_word := map(getLowercase, input("Введите слово: "))) != "":
    if (input_word in synonyms): print(f"Синонимы: {map(getCapitalize, synonyms[input_word])}")
    else: print("Такого слова в словаре нет.")