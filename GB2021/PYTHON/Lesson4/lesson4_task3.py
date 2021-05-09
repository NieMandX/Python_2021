# Python basics. Homework 4. 2021.
# ..................................

# -------
# Task 3.
# -------

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# method 1

list_1 = [k for k in range(20, 241) for i in [20, 21] if not k % i]

# method 2

list_2 = [k for k in range(20, 241) if (not k % 20) or (not k % 21)]

print(list_1)
print(list_1)

