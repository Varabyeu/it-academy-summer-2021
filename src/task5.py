"""Написать программу которая находит ближайшую степень двойки
 к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def the_closest_to_two(first_num):
    iterator = 0
    num = first_num
    while num / 2 > 1:
        num = num / 2
        iterator += 1
    if (first_num - 2 ** iterator) / 2 ** iterator >= 0.5:
        return 'Ближайшая степень ' \
               'двойки будет {}'.format(2 ** (iterator + 1))
    else:
        return 'Ближайшая степень ' \
               'двойки будет {}'.format(2 ** iterator)


inputted_num = int(input('Введите число: '))
print(the_closest_to_two(inputted_num))
