# Python basics. Homework 3. 2021.
# ..................................

# -------
# Task 4.
# -------

# 4. Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо
# обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

# Version 1
# ---------

def my_func_1(x, y):
    
    if x > 0 and y < 0 and type(y) == int:
        
        return x ** y
    
    else:
        
        return 'ERROR: X must be positive, Y must be negative integer !!!'

# Version 2
# ---------

def my_func_2(x, y):
    
    if x > 0 and y < 0 and type(y) == int:
        
        accum = 1
        for _ in range(abs(y)):
            accum *= x
        
        return 1 / accum
    
    else:
        
        return 'ERROR: X must be positive, Y must be negative integer !!!'    
    
print(my_func_1(2, -3))