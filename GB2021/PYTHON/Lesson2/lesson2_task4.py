# Python basics. Homework 2. 2021.
# ..................................

# -------
# Task 4.
# -------

# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.

wordlist = input('Пожалуйста, введите строку из нескольких слов разделенными пробелами: ').split(' ')
print('\n')
for ind, word in enumerate(wordlist):
    print(f'{ind + 1}. {word[:10]}')
