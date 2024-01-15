def isPalindrome(word: str) -> bool:
    for i in range(len(word) // 2):
        if (word[i] != word[-(i + 1)]):
            return False
    return True


user_input = input("Введите слово: ")
print(f"Слово {'' if isPalindrome(user_input) else 'не '}является палиндромом")