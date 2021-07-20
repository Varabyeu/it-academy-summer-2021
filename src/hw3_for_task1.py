"""
Homework3 module with all tasks for task1 in homework5
"""

import copy


def task2_hw3():
    """List practice

    Используйте генератор списков чтобы получить
    следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    """

    lst_f_l = "ab"
    lst_s_l = "bcd"
    list_gen = [f_l + s_l for f_l in lst_f_l for s_l in lst_s_l]
    print(list_gen)

    """
    Используйте на предыдущий список slice чтобы
    # получить следующий: ['ab', 'ad', 'bc'].
    """

    sliced_list = list_gen[::2]
    print(sliced_list)

    """Используйте генератор списков чтобы получить
    следующий ['1a', '2a', '3a', '4a'].
    """

    list_num_and_a = [str(num) + "a" for num in range(1, 5)]
    print(list_num_and_a)

    """Одной строкой удалите элемент  '2a' из прошлого
    списка и напечатайте его."""

    print(list_num_and_a.pop(1))

    """
    Скопируйте список и добавьте в него элемент
    '2a' так чтобы в исходном списке этого элемента не было.
    """

    new_list = copy.deepcopy(list_num_and_a)
    new_list.append("2a")
    print(new_list)


def task3_hw3():
    """
    Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    """

    list_abc = ['a', 'b', 'c']
    tuple_of_list_abc = tuple(list_abc)
    print(tuple_of_list_abc)

    """
    Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    """
    tuple_abc = ('a', 'b', 'c')
    list_of_tuple_abc = list(tuple_abc)
    print(list_of_tuple_abc)

    """Сделайте следующие присвоения одной строкой 
    a = 'a', b=2, c=’python’."""

    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    """
    Создайте кортеж из одного элемента, чтобы при итерировании по этому
    элементы последовательно выводились значения 1, 2, 3.
    Убедитесь что len() исходного кортежа возвращает 1.
    """

    tuple_one_el = ([1, 2, 3],)
    for element in tuple_one_el[0]:
        print(element)
    print(len(tuple_one_el))


def task4_hw3():
    """
    Дан список чисел. Посчитайте, сколько в нем пар элементов,
    равных друг другу. Считается, что любые два элемента,
    равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """

    list_num = [1, 2, 3, 4, 4, 2, 3, 1, 2, 1]
    list_num_new = []
    list_count = []

    for element in list_num:
        if list_num.count(element) > 1 and element not in list_num_new:
            list_num_new.append(element)
            list_count.append(list_num.count(element))
            cal = 1
            net = 0
            cal_list = []
            sum_all = 0
            for el_count in list_count:
                while el_count - cal > 0:
                    net += el_count - cal
                    cal += 1
                cal_list.append(net)
                cal = 1
                net = 0
            for el_for_sum in cal_list:
                sum_all += el_for_sum
    print(sum_all)


def task5_hw3():
    """
    Дан список. Выведите те его элементы, которые встречаются в списке
    только один раз. Элементы нужно выводить в том порядке, в котором
    они встречаются в списке.
    """

    list_num = [0, 1, 3, 5, 7, 2, 3, 1, 2, 1]
    list_num_new = []

    for element in list_num:
        if list_num.count(element) == 1:
            list_num_new.append(element)
    print(list_num_new)


def task6_hw3():
    """
    Дан список целых чисел. Требуется переместить все ненулевые
    элементы в левую часть списка, не меняя их порядок, а все
    нули - в правую часть. Порядок ненулевых элементов изменять
    нельзя, дополнительный список использовать нельзя, задачу н
    ужно выполнить за один проход по списку. Распечатайте
    полученный список.
    """

    list_num = [0, 1, 0, 2, 0, 3, 4, 5, 6]
    cal = 0
    x = list_num.count(0)
    while cal < x:
        list_num.append(list_num[list_num.index(0)])
        list_num.remove(0)
        cal += 1
    print(list_num)

