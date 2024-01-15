from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

newFloats = list(map(lambda number: round(number ** 3, 3), floats))
newNames = list(filter(lambda name: len(name) == 5, names))
newNumbers = reduce(lambda counter, item: counter * item, numbers)