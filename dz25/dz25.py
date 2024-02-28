data_lst = ['1', '2', '3', '4d', 5]

new_list = []

for item in data_lst:
    try:
        num = int(item)
        new_list.append(num)
    except ValueError:
        print(f"Данные невалидны: {item}")

print(f"Новый список: {new_list}")