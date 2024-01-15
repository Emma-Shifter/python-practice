import collections

lessChar = 65
greaterChar = 122

with open("text.txt", "r", encoding="UTF-8") as file:
    clean_string = "".join([
        char.lower() for char in file.read() if lessChar <= ord(char) <= greaterChar
    ])

cleanString = collections.Counter(clean_string)
characters = sorted([(cleanString[letter], letter)
                          for letter in cleanString.keys()], key=lambda t: (-t[0], t[1]))
totalChars = sum(i[0] for i in characters)
line_break = "\n"

with open("analysis.txt", "w", encoding="UTF-8") as file:
    file.write(f"{line_break.join([f'{i[1]} {round(i[0] / totalChars, 3)}' for i in characters])}")