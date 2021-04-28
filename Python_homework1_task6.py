'''

6. 
-----------------------------------------------------------------

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена
составить не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.

Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

-----------------------------------------------------------------
'''

print('\n' * 1)
print(f'{"Python basics. Homework 1. Exercise 6.":>60}')
print('-' * 60)
print('\n')


dist = int(input('Input a first day distance, please: '))
stop_dist = int(input('Input a disired distance :'))
day_counter = 1

print('\n')

print(f'day {day_counter}: {dist:.2f}')

if dist:
    while dist < stop_dist:
        day_counter += 1
        dist += dist * .1
        print(f'day {day_counter}: {dist:.2f}')
        
    print('\n')    
    print(f'On the {day_counter} day athlete ran at least: {dist:.2f} km.')
    print('\n')

else:
    day_counter += 1
    print(f'day {day_counter}: {dist:.2f}')
    print('\n')
    print('Hmm...)) maybe we`ll take at least one step?')
    print('\n')