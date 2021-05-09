# Python basics. Homework 4. 2021.
# ..................................

# -------
# Task 4.
# -------

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

list_len = 20

list1 = [randint(0, 9) for _ in range(list_len)]

def counter (n, l):
    count = 0
    for val in l:
        count += int(val == n)
    return count

result = [num for num in list1 if counter(num, list1) == 1]

print(list1)
print(result)