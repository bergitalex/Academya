word = input("Введите слово: ")
palindrome = word.lower()
if palindrome == word.lower()[::-1]:
    print(f"Обнаружен палиндром: {word}")
else:
    print(f'Слово "{word}" не является палиндромом!')
