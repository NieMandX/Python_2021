# Python basics. Homework 5. 2021.
# ..................................

# -------
# Task 2.
# -------

# 2. Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк, количества
# слов в каждой строке.

def words_counter(filename):
    
    f = open(filename, 'r')
    words_count = {}

    for line_number, line in enumerate(f):
        words_in_line = line.split()
        words_count[line_number + 1] = len(words_in_line)
    
    f.close()
    
    return words_count

words_dict = words_counter('homework5_task2.txt')
lines_number = len(words_dict)
print('\n')

if lines_number == 0:
    print('Text file is empty.')

else:
    print(f'Text file contains {lines_number} lines.')
    print('\n')
    for k, v in words_dict.items():
        print(f'Line ... {k:3} contains {v:2} words')