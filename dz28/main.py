import json

def load_cities_set():
    with open('cities.json', 'r', encoding='utf-8') as json_file:
        return set(json.load(json_file))

def user_turn(available_cities):
    user_input = input("Ваш ход (название города): ").strip().title()
    return user_input

def computer_turn(last_letter, available_cities):
    for city in available_cities:
        if city[0].lower() == last_letter:
            return city
    return None

def play_game():
    cities_set = load_cities_set()
    used_cities = set()
    last_letter = None

    while True:
        user_input = user_turn(cities_set - used_cities)

        if user_input.lower() == "стоп":
            print("Вы проиграли! Компьютер победил")
            break

        if user_input not in cities_set or user_input in used_cities:
            print("Такого города нет в списке или он уже использован. Вы проиграли компьютеру.")
            break

        used_cities.add(user_input)
        last_letter = user_input[-1].lower()

        computer_city = computer_turn(last_letter, cities_set - used_cities)

        if computer_city is None:
            print("Компьютер не смог найти подходящий город. Вы выиграли!")
            break

        print(f"Компьютер: {computer_city}")
        used_cities.add(computer_city)

    print("Игра завершена!")

def main():
    play_game()

if __name__ == "__main__":
    main()
