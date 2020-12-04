# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    latin_char = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Введите строку из слов, разделенных пробелами ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
