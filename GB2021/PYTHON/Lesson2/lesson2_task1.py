# Python basics. Homework 2. 2021.
# ..................................

# -------
# Task 1.
# -------

# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.


list_1 = [128, 3.1415, 'Triangle', True, None, [128, 110, 34],
         ('Red', 'Green', 'Blue'), {'Tree': [45, 20, 50], 'House': []}]

for element in list_1:
    print(type(element))