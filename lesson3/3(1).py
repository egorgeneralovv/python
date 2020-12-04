# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        arg1 = int(input('Введите первое число: '))
        arg2 = int(input('введите второе число: '))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Неправильное число! Нельзя использовать ноль в качестве знаменателя'
    return res

print(f'result {div()}')
