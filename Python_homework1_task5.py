'''

5. 
-----------------------------------------------------------------

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.

-----------------------------------------------------------------
'''

print('\n' * 1)
print(f'{"Python basics. Homework 1. Exercise 5.":>60}')
print('-' * 60)
print('\n')

revenues = int(input('Input a company revenues, please: '))
costs = int(input('Input a company costs, please: '))
employees = int(input('Input a number of employees, please: '))

profit = revenues - costs

if profit > 0:
    print('\n')
    print(f'{"*" * 31:^60}')
    print(f'{"* Your company is profitable. *".upper():^60}')
    print(f'{"*" * 31:^60}')
    print('\n')

    print(f'Profitability of proceeds is: {profit / revenues:>30.2f}')
    print(f'Profit by emloyee is: {profit / employees:>38.2f}')

else:
    print('\n')
    print(f'{"o" * 31:^60}')
    print(f'{"o Your company is unprofitable. o".upper():^60}')
    print(f'{"o" * 31:^60}')
    print('\n')
    
print('\n')