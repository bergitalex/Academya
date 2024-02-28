from typing import Callable


def password_checker(func: Callable) -> Callable:
    def wrapper(password: str) -> str:
        if len(password) < 8:
            return "Ошибка: Пароль должен содержать не менее 8 символов"
        # наличия цифр
        if not any(char.isdigit() for char in password):
            return "Ошибка:  Пароль должен содержать хотя бы одну цифру"
        # наличия заглавных букв
        if not any(char.isupper() for char in password):
            return "Ошибка: Пароль должен содержать хотя бы одну заглавную букву"
        # наличия строчных букв
        if not any(char.islower() for char in password):
            return "Ошибка: Пароль должен содержать хотя бы одну строчную букву"
        # наличия спецсимволов
        if not any(char in "!@#$%^&*()-_+=~`[]{}|;:,.<>?/" for char in password):
            return "Ошибка:  Пароль должен содержать хотя бы один спецсимвол."
        return func(password)
    return wrapper

@password_checker
def register_user(password: str) -> str:
    return "Пользователь зарегистрирован"


print(register_user("weakpassword"))  # должно вывести -- Ошибка пасворд должен содержать хотя бы одну заглавную букву
print(register_user("WeakPassword!"))  # Ошибка  не соответствует требованиям сложности
print(register_user("weakpassword123!"))  # Пароль не содержащий заглавную букву
print(register_user("WeakPassword123"))  # должен содержать хотя бы один спецсимвол
print(register_user("Password123!"))  # должно вывести --  пользователь зарегистрирован