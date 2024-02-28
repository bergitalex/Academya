from cities import cities_list

cities_set = set()

for city_info in cities_list:
    cities_set.add(city_info["name"])
while True:
    user_input = input("Ваш ход (название города): ").strip().title()
    if user_input.lower() == "стоп":
        print("Вы проиграли! Компьютер победил")
        break
    if user_input not in cities_set:
        print("Такого города нет в списке. Вы проиграли")
        break
    cities_set.remove(user_input)
    last_letter = user_input[-1].lower()
    computer_city = None
    for city_info in cities_list:
        if city_info["name"].lower().startswith(last_letter) and city_info["name"] in cities_set:
            computer_city = city_info["name"]
            cities_set.remove(computer_city)
            break
    #наличие города
    if computer_city is None:
        print("Компьютер не смог найти подходящий город. Вы выиграли!")
        break
    print(f"Компьютер: {computer_city}")

# Объявим победителя
if len(cities_set) % 2 == 0:
    print("Поздравляем, вы победили!")
else:
    print("Вы проиграли. Компьютер выиграл")