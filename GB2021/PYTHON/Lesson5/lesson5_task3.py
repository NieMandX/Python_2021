# Python basics. Homework 5. 2021.
# ..................................

# -------
# Task 3.
# -------

# 3. Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов. Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

filename = 'homework5_task3.txt'

f = open(filename, 'r')
less_20k = []
employees = []
total_salary = 0

for ind, line in enumerate(f):
    employee = line.split(',')
    employees.append(employee)
    total_salary += float(employee[1])
    if float(employee[1]) < 20000:
        less_20k.append(employee)
    
f.close()

print('\n')
print(f'Average salary = {total_salary / len(employees)}')
print('\n')
print('List of employees with salary less than 20k')
print('-' * 44)
for row in less_20k:
    print(f'{row[0]:<30}....{row[1]:>10}')