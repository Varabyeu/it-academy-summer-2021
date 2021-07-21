"""Homework4 module with all tasks for task1 in homework5"""


def task1_hw4():
    """Создание генератора словарей

    Создайте словарь с помощью генератора словарей,
    так чтобы его ключами были числа от 1 до 20,
    а значениями кубы этих чисел.
    """

    dict_cube = {key: key ** 3 for key in range(1, 21)}
    print(dict_cube)


def task2_hw4(num_countries=2, num_cities=2):
    """Выведите страну по городу

    Дан список стран и городов каждой страны.
    Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные
    Программа получает на вход количество стран N.
    Далее идет N строк, каждая строка начинается с названия
    страны, затем идут названия городов этой страны. В следующей
    строке записано число M, далее идут M запросов — названия каких-то
    M городов, перечисленных выше.
    Выходные данные
    Для каждого из запроса выведите название страны, в котором находится
    данный город.
    """
    list_country_cities = [
        ['Russia', 'Moscow', 'SpB'],
        ['Ukraine', 'Kiev', 'Lviv']
    ]
    list_searching_cities = ['Moscow', 'Lviv']
    country_cities_inputted = []
    cities_input = []

    for position in range(num_countries):
        country_cities_inputted.append(list_country_cities[position])

    for every_city in list_searching_cities:
        cities_input.append(every_city)

    for city in cities_input:
        for country_city in country_cities_inputted:
            if city in country_city:
                print(country_city[0])


def task3_hw4():
    """Сколько различных чисел в списках

    Даны два списка чисел. Посчитайте, сколько различных чисел
    содержится одновременно как в первом списке, так и во втором
    """

    first_num_list = [1, 2, 3, 7]
    second_num_list = [1, 2, 34]

    list_unicl_numbrs = []
    for elmnt in first_num_list:
        if elmnt not in second_num_list:
            list_unicl_numbrs.append(elmnt)
    for el in second_num_list:
        if el not in first_num_list:
            list_unicl_numbrs.append(el)
    count_unicl_numbrs = len(list_unicl_numbrs)
    print(count_unicl_numbrs)


def task4_hw4():
    """Сколько различных чисел в списках

    Даны два списка чисел. Посчитайте, сколько различных чисел
    содержится одновременно как в первом списке, так и во втором
    """

    first_num_list = [1, 2, 3, 7]
    second_num_list = [1, 2, 34]

    list_unicl_numbrs_frst = []
    list_unicl_numbrs_scnd = []
    for elmnt in first_num_list:
        if elmnt not in second_num_list:
            list_unicl_numbrs_frst.append(elmnt)
    for el in second_num_list:
        if el not in first_num_list:
            list_unicl_numbrs_scnd.append(el)
    count_unicl_numbrs_frst = len(list_unicl_numbrs_frst)
    count_unicl_numbrs_scnd = len(list_unicl_numbrs_scnd)
    print("В первом списке количество "
          "различных чисел - {}.".format(count_unicl_numbrs_frst))
    print("Во втором списке количество "
          "различных чисел - {}.".format(count_unicl_numbrs_scnd))


def task5_hw4():
    """Школьники и языки

    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников.
    """

    pupil1_langs = ['Russian', 'English']
    pupil2_langs = ['Russian', 'Belarusian', 'English']
    pupil3_langs = ['Russian', 'Italian', 'French']
    pupil_all_langs = set(pupil1_langs + pupil2_langs + pupil3_langs)
    print("Количество языков, которые знают "
          "ученики - {}: ".format(len(pupil_all_langs)))
    for langs in pupil_all_langs:
        print(langs)
    set_p1 = set(pupil1_langs)
    set_p2 = set(pupil2_langs)
    set_p3 = set(pupil3_langs)
    one_more_lang = set_p1 & set_p2 & set_p3
    print("Количество языков, "
          "которые знает хотя бы "
          "один ученик - {}: ".format(len(one_more_lang)))
    for lang in one_more_lang:
        print(lang)


def task6_hw4():
    """Сколько различных слов в тексте

    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или
    большим числом пробелов или символами конца строки. Определите,
    сколько различных слов содержится в этом тексте.
    """

    input_text = "Текст написан и с пробелом одним и  двумя пробелами!"
    splitted_text = input_text.split()
    lst_of_unique_words = []
    for word in splitted_text:
        if word not in lst_of_unique_words:
            lst_of_unique_words.append(word)
    num_of_dif_words = len(lst_of_unique_words)
    print(num_of_dif_words)


def task7_hw4(first_num=12, second_num=36):
    """Задача на наибольший общий делитель

    Даны два натуральных числа. Вычислите их наибольший общий делитель
    при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    """

    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    nod = first_num + second_num
    print(nod)
