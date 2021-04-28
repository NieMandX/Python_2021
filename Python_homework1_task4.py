'''

4.  
-----------------------------------------------------------------

Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

-----------------------------------------------------------------
'''

print('\n' * 1)
print(f'{"Python basics. Homework 1. Exercise 4.":>60}')
print('-' * 60)
print('\n')

number = int(input('Input any positive integer, please: '))
print('\n')

max = 0

while number:
    
    lsd = number % 10
    number //= 10
    
    if lsd > max:
        max = lsd 

print(f'Maximum digit in your number is: {max}')
print('\n')