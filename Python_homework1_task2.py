'''
2.
----------------------------------------------

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды 
и выведите в формате чч:мм:сс.
Используйте форматирование строк.

----------------------------------------------
'''

print('\n' * 2)
print(f'{"Homework 1. Exercise 2.":>60}')
print('-' * 60)
print('\n')

sec = int(input('Enter any time in seconds, please: '))

t_sec = sec % 60
t_min = sec // 60 % 60
t_hrs = sec // 60 // 60 % 24

print(f'Your time in (HH:MM:SS) format is: {t_hrs:02d}:{t_min:02d}:{t_sec:02d}')
print('\n' * 1)