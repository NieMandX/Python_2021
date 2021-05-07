# Python basics. Homework 3. 2021.
# ..................................

# -------
# Task 5.
# -------

# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
print('\n')
print('.' * 60)
print(f'{"Введите строку чисел, разделяя их пробелом.":^60}')
print(f'{"Подтвердите ввод строки при помощи Enter.":^60}')
print(f'{"Для завершения работы перед Enter введите *":^60}')
print('.' * 60)
print('\n')

flag = False
alphabet = '0123456789.-'
summ = 0

while not flag:

    line = input('Введите строку: ')
    flag = line.endswith('*')
    line = line.split()
    
    block = '0'

    for word in line:
        sign_flag = 1
        count = 0
        for ind, char in enumerate(word):
            if char in alphabet:
                if char == '.':
                    count += 1
                    if count > 1:
                        pass
                    else:
                        block += char

                elif char == '-' and ind == 0:
                    sign_flag = -1

                elif char == '-' and ind != 0:
                    pass

                else:
                    block += char

        summ += (float(block) * sign_flag)
        block = '0'

print('\n')
print(f'Сумма всех введенных чисел: {summ}')