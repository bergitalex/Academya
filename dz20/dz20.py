# Задание №1
seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"В указанном количестве секунд ({seconds}):"
      f"\nЧасов: {hours}"
      f"\nМинут: {minutes}"
      f"\nСекунд: {remaining_seconds}")

# Задание №2
celsius = float(input("Введите температуру в градусах Цельсия: "))

kelvin = round(celsius + 274.15, 2)
fahrenheit = round(celsius * 9/5 + 32, 2)
reomur = round(celsius * 4/5, 2)

print(f"В указанном количестве градусов цельсия: {celsius}:"
      f"\nГрадусов Кельвина: {kelvin}"
      f"\nГрадусов Фаренгейта: {fahrenheit}"
      f"\nГрадусов Реомюра: {reomur}")
