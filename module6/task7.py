import collections

arr1 = [1, 5, 10, 20, 40, 80, 100]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

dict1 = collections.Counter(arr1)
dict2 = collections.Counter(arr2)
dict3 = collections.Counter(arr3)

set1 = set(arr1)
set2 = set(arr2)
set3 = set(arr3)

print(f"Задача 1:\n"
      f"Решение без множеств: {[key for key in dict1.keys() if key in dict2 and key in dict3]}\n"
      f"Решение с множествами: {set1.intersection(set2).intersection(set3)}")
print(f"Задача 2:\n"
      f"Решение без множеств: {[key for key in dict1.keys() if key not in dict2 and key not in dict3]}\n"
      f"Решение с множествами: {set1.difference(set2).difference(set3)}")