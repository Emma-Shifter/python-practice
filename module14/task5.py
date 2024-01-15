import functools
from typing import Callable, Any, Dict

HASH: Dict[Callable, Dict[Any, Any]] = dict()
def hashed(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        hashfunction = {}
        if func in HASH:
            hashfunction = HASH[func]
            if (args in hashfunction): return HASH[func][args]
        res = func(*args, **kwargs)
        hashfunction[args] = res
        HASH[func] = hashfunction
        return res
    return wrapper

@hashed
def fibonacci(n: int) -> int:
    if (n <= 1): return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(200))