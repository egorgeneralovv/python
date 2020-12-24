# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
for el in count(int(input('Введите стартовое число - '))):
     print(el)
...
from itertools import cycle
my_list = [True, 'HNY', 2021, None]
for el in cycle(my_list):
    print(el)
