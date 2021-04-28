'''
1.  
-----------------------------------------------------------------

Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.

-----------------------------------------------------------------
'''

print('\n' * 1)
print(f'{"Python basics. Homework 1. Exercise 1.":>60}')
print('-' * 60)
print('\n')

first_name = input('Enter your First Name, please: ')
last_name = input('Enter your Last Name, please: ')
height = float(input('Enter your height (m), please: '))
weight = float(input('Enter your First weigth (kg), please: '))
age = int(input('Enter your age, please: '))


offset = 40 - len(last_name) - 1
print('\n')
print(f'{first_name:>{offset}} {last_name:>}')
print('.' * 40)
print('\n')
print(f'height (m): {height:>28.2f}')
print(f'weight (kg): {weight:>27.2f}')
print(f'age: {age:>35.2f}')
print('\n')