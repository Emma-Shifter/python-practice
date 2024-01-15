import functools
from typing import Callable, Any
user_permissions = {'admin'}

def checkPermission(permission: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if (permission in user_permissions): return func(*args, **kwargs)
            raise PermissionError(f"у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
        return wrapper
    return decorator

@checkPermission('admin')
def delete_site() -> None:
    print('Удаляем сайт')

@checkPermission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')

delete_site()
add_comment()