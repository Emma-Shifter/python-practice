import random
import os

totalSum = 0
hasError = False
outputFile = os.path.join("out_file.txt")

if os.path.exists(outputFile): os.remove(outputFile)
try:
    while totalSum < 777:
        userNumber = int(input("Введите число: "))
        if (random.randint(0, 13) == 6): raise RuntimeError
        totalSum += userNumber
        with open(outputFile, "a", encoding="UTF-8") as file:
            file.write(str(userNumber) + "\n")
except RuntimeError:
    hasError = True
    print("Вас постигла неудача!")
else: print("Вы успешно выполнили условие для выхода из порочного цикла!")