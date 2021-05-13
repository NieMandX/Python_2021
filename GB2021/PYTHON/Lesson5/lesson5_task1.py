# Python basics. Homework 5. 2021.
# ..................................

# -------
# Task 1.
# -------

# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('homework5_task1.txt', 'w')
line = input('Enter text: ')

while line != '':
    f.write(line + '\n')
    line = input('Enter text: ')

f.close()