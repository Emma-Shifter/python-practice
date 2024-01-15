import functools
import time
from typing import Callable, Any

class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
    def __call__(self, *args, **kwargs) -> Any:
        print(f"Вызов функции {self.func.__name__}\n"
              f"Аргументы: {args}, {kwargs}")
        timeStart = time.time()
        functionResult = self.func(*args, **kwargs)
        print(f"Результат: {functionResult}\n"
              f"Время выполнения: {time.time() - timeStart} секунд")
        return functionResult

@LoggerDecorator
def complex_algorithm(arg1, arg2) -> Any:
    algorithmRes = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                algorithmRes += i + j
    return algorithmRes

result = complex_algorithm(10, 50)