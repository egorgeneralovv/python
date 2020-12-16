# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, birthday, city, email, phone):
    return f'name - {name}; surname - {surname}; birthday - {birthday}; city - {city};' \
           f'email - {email}; phone - {phone};'

name = input('введите имя- ')
surname = input('введите фамилию- ')
birthday = input('введите год- ')
city = input('введите город- ')
email = input('введите адрес электронной почты- ')
phone = input('введите номер телефона- ')

print(my_func(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))





