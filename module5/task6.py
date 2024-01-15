def getCompress(string: str) -> str:
    res = ""
    last_char = None
    chars_count = 0
    for char in string:
        if (char != last_char):
            if (last_char is not None): res += f"{last_char}{chars_count}"
            last_char = char
            chars_count = 0
        chars_count += 1

    if (chars_count > 0): return res + f"{last_char}{chars_count}"

print(f"Закодированная строка: {getCompress(input('Введите строку: '))}.")