# Python basics. Homework 4. 2021.
# ..................................

# -------
# Task 2.
# -------

# 2. Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint
from functools import reduce

list_len = 20

int_list = [randint(0, 1000) for _ in range(list_len)]


new_list = [val for ind, val in enumerate(int_list) if val > int_list[ind - 1 % (ind + 1)]]

print(int_list)
print(new_list)