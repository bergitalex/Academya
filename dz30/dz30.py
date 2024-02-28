from typing import Dict, Any
from pprint import pprint
from marvel import full_dict

user_input = input("Введите ID фильмов через пробел: ")

# 2. Разбивка на список и преобразование в int
ids = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

# 3. Фильтрация словаря по ID
filtered_dict = {
    id: movie
    for id, movie in full_dict.items()
    if id in ids
}

# 4.множество режиссеров
directors = {movie["director"] for movie in full_dict.values() if movie}

# 5. копия словаря с str(year)
str_year_dict = {
    id: {**movie, "year": str(movie["year"])}
    for id, movie in full_dict.items()
}

# 6. Фильтрация словаря по названиям на букву Ч
starts_with_ch_dict = {
    id: movie
    for id, movie in filtered_dict.items()
    if movie and "title" in movie and movie["title"].startswith("Ч")
}

# 7. Сортировка по году c lambda
valid_movies = {id: movie for id, movie in full_dict.items() if isinstance(movie['year'], int)}

def get_sort_key(item):
    year_value = item[1]["year"]
    return (int(year_value) if isinstance(year_value, int) else float('inf'))

sorted_by_year = sorted(
    valid_movies.items(), key=get_sort_key)

# 8. Сортировка по году и режиссеру c lambda
def get_sort_key_year_and_director(item):
    year_value = item[1]["year"]
    return (int(year_value) if isinstance(year_value, int) else float('inf'), item[1]["director"])

sorted_by_year_and_director = sorted(
    full_dict.items(),
    key=get_sort_key_year_and_director,
)

# 9. filter и sorted
filtered_and_sorted = sorted(
    filter(lambda item: item[0] in ids, full_dict.items()),
    key=lambda item: item[1]["year"],
)

# 10. Аннотация типов и проверка mypy
# домашки\dz30> mypy main.py
# Success: no issues found in 1 source file

# 11

print("Задание 3: Фильтрация по ID")
pprint(filtered_dict, sort_dicts=False)

print("Задание 4: Множество режиссеров")
pprint(directors)

print("Задание 5: Копия словаря с str(year)")
pprint(str_year_dict, sort_dicts=False)

print("Задание 6: Фильтрация по названиям на букву Ч")
pprint(starts_with_ch_dict, sort_dicts=False)

print("Задание 7: Сортировка по году")
pprint(sorted_by_year, sort_dicts=False)

print("Задание 8: Сортировка по году и режиссеру")
pprint(sorted_by_year_and_director, sort_dicts=False)

print("Задание 9: Однострочник: filter + sorted")
pprint(filtered_and_sorted, sort_dicts=False)
