# Задача №1
phone_number = input("Введите номер телефона: ")

# Убираем кобки
clean_number = ''.join(filter(str.isdigit, phone_number))

if len(clean_number) == 11:
    if clean_number.startswith('8') or clean_number.startswith('7'):
        print("Номер телефона правильный")
    else:
        print("Номер телефона должен начинаться на 8 или +7.")
else:
    print("Неверная длина номера телефона.")

# Задача №2
password = input("Введите пароль: ")

# если есть спец символ
if any(char in password for char in '!@#$%^&*()-_=+[]{}|;:,.<>?'):
    # если без пробелов
    if ' ' not in password:
        # разной высоты буквы присутствуют
        if any(char.islower() for char in password) and any(char.isupper() for char in password):
            # если длинна больше 7
            if len(password) > 7:
                print("Пароль надежный")
            else:
                print("Пароль должен быть более 7 символов длиной")
        else:
            print("Пароль должен содержать большие и маленькие буквы")
    else:
        print("Пароль не должен содержать пробелов")
else:
    print("Пароль должен содержать хотя бы один спецзнак")