import functools
import time
from typing import Callable, Any

def waitForCalling(seconds: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@waitForCalling(seconds=2)
def do_something():
    print("doing...")

do_something()