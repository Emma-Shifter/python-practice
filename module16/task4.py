import functools
from typing import Callable, Any

def decoratorWithArgs(func: Callable) -> Callable:
    @functools.wraps(func)
    def decorator(*args, **kwargs) -> Any:
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func
    return decorator

@decoratorWithArgs
def decoratedDecorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper

@decoratedDecorator(100, 'рублей', 200, 'друзей')
def dcoratedFunction(text: str, num: int) -> None:
    print("Привет", text, num)

dcoratedFunction("Юзер", 101)