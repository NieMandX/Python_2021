'''
3.
----------------------------------------------

Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

----------------------------------------------
'''

print('\n' * 1)
print(f'{"Homework 1. Exercise 3.":>60}')
print('-' * 60)
print('\n')

number = input('Input any integer, please: ')
print('\n')

if int(number) < 0:
    multiplier = -1
    number = str(-1 * int(number))
    sign = '-'
    
else:
    multiplier = 1
    sign = '+'

count = 3
summ = 0

while count:
    summ += int(count * number)
    print(f'{multiplier * int(count * number):>60}')
    print(f'{"+" * (1 % count) :>60}')
    count -= 1
    
print(f'Result is: {multiplier * summ:>49}')
print('\n')