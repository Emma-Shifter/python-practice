import collections

def getPalindrome(string: str) -> bool:
    letters_count = collections.Counter(string)
    return sum(1 for key in letters_count.keys() if letters_count[key] % 2 == 1) <= 1

print(f"{'Можно' if getPalindrome(input('Введите строку: ')) else 'Нельзя'} сделать палиндромом")