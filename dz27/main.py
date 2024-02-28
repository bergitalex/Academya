import json

# №получение сета городов и запись его в JSON)
# from cities import cities_list
# cities_set = set()
# for city_info in cities_list:
#     cities_set.add(city_info["name"])
#
# # запись в JSON
# with open('cities_set.json', 'w', encoding='utf-8') as json_file:
#     json.dump(list(cities_set), json_file, ensure_ascii=False)

# для чтения данных из JSON и загрузки готового датасета
with open('cities_set.json', 'r', encoding='utf-8') as json_file:
    loaded_cities_set = set(json.load(json_file))
    print("Загруженный датасет из JSON:", loaded_cities_set)


# while True:
#     user_input = input("Ваш ход (название города): ").strip().title()
#     if user_input.lower() == "стоп":
#         print("Вы проиграли, компьютер победил")
#         break
#     if user_input not in loaded_cities_set:
#         print("Такого города нет. Вы проиграли")
#         break
#     loaded_cities_set.remove(user_input)
#     last_letter = user_input[-1].lower()
#     computer_city = None
#     for city_info in cities_list:
#         if city_info["name"].lower().startswith(last_letter) and city_info["name"] in loaded_cities_set:
#             computer_city = city_info["name"]
#             loaded_cities_set.remove(computer_city)
#             break
#
#     if computer_city is None:
#         print("Компьютер не смог найти город.Вы выиграли")
#         break
#     print(f"Компьютер: {computer_city}")
#
#
# if len(loaded_cities_set) % 2 == 0:
#     print("Поздравляем, вы победили!")
# else:
#     print("Вы проиграли. Компьютер выиграл")
