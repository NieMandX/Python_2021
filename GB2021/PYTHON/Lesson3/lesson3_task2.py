# Python basics. Homework 3. 2021.
# ..................................

# -------
# Task 2.
# -------

# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна
# принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_card(firstname, lastname, birthyear, city, email, phone):
    
    user_dict = {'firstname': firstname, 'lastname': lastname,
                        'birthyear': birthyear, 'city': city, 'email': email, 'phone': phone}
    
    user_string = ','.join([str(_) for _ in user_dict.values()])
    
    return user_string

# Не совсем понял в каком виде нужно возвращать результат из функции
# попробовал строкой с разделителем ))) 

user_data = user_card(firstname = 'John', lastname = 'Doyl',
                      birthyear = 1990, city = 'Moscow', email = 'johndoyl@server.com', phone = 89001103434)
print(user_data)