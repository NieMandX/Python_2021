# Python basics. Homework 2. 2021.
# ..................................

# -------
# Task 2.
# -------

# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_2 = input('Введите несколько элементов списка, разделяя их запятыми: ').split(',')

for i, _ in enumerate(list_2):
    offset = i % 2
    list_2[i], list_2[i - offset] = list_2[i - offset], list_2[i]
    
print(list_2)