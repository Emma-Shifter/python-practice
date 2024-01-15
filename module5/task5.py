def isPasswordCorrect(password: str) -> bool:
    bigLetters = False
    numbers_count = 0
    for i in password:
        if (bigLetters and numbers_count >= 3): break
        if (i.isupper()): bigLetters = True
        elif (i.isdigit()): numbers_count += 1
    return len(password) >= 8 and bigLetters and numbers_count >= 3


while not isPasswordCorrect(input("Придумайте пароль: ")):
    print("Пароль ненадёжный. Попробуйте ещё раз.")
print("Это надёжный пароль.")