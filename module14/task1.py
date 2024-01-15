import functools
from typing import Callable, Any

def howAreYou(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)
    return wrapper

@howAreYou
def test() -> None:
    print('<Тут что-то происходит...>')

test()