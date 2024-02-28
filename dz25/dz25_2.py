phone_number = input("Введите номер: ")

cleaned_number = ''.join(filter(str.isdigit, phone_number))
if len(cleaned_number) != 11:
    raise ValueError(f'Номер телефона {phone_number} не содержит 11 цифр')

if not (cleaned_number.startswith('8') or cleaned_number.startswith('7')):
    raise ValueError(f'Номер телефона {phone_number} не начинается с 8 или +7')

if not cleaned_number.isdigit():
    raise ValueError(f'Номер телефона {phone_number} содержит недопустимые символы')

print("номер телефонов валиден")
