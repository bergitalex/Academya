import csv
from functools import wraps
from typing import Callable

def password_validator(min_length: int = 8, min_uppercase: int = 1,
                       min_lowercase: int = 1, min_special_chars: int = 1) -> Callable:
    """
    Декоратор для валидации паролей.
    Параметры:
    min_length(int):минимальная длина пароля (по умолчанию 8).
    min_uppercase(int):минимальное количество букв верхнего регистра (по умолчанию 1).
    min_lowercase(int):минимальное количество букв нижнего регистра (по умолчанию 1).
    min_special_chars(int):минимальное количество спец-знаков (по умолчанию 1).
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(username: str, password: str) -> None:
            # Проверяем длину пароля
            if len(password) < min_length:
                raise ValueError(f"Пароль должен содержать минимум {min_length} символов.")
            # Проверяем количество букв верхнего регистра
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f"Пароль должен содержать минимум {min_uppercase} букв верхнего регистра.")
            # Проверяем количество букв нижнего регистра
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f"Пароль должен содержать минимум {min_lowercase} букв нижнего регистра.")
            # Проверяем количество спец-знаков
            if sum(1 for char in password if char in '!@#$%^&*()-_=+[]{}|;:,.<>?`~') < min_special_chars:
                raise ValueError(f"Пароль должен содержать минимум {min_special_chars} спец-знака.")
            return func(username, password)
        return wrapper
    return decorator

def username_validator(func: Callable)  -> Callable:
    """
    Декоратор для валидации имени пользователя (отсутствие пробелов).
    """
    @wraps(func)
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError("Имя пользователя не должно содержать пробелов.")
        return func(username, password)
    return wrapper

@password_validator()
@username_validator
def register_user(username: str, password: str) -> None:
    """
    Функция для регистрации нового пользователя.
    Параметры:
    username(str): Имя пользователя.
    password(str): Пароль пользователя.
    Raises:
    ValueError: Если пароль или юзернейм не соответствует заданным условиям.
    """
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

# Примеры использования
# Тестирование успешного случая
try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю 
try:
    register_user("JaneSmith", "weak")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по юзернейму
try:
    register_user("John Doe", "StrongPassword123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")
