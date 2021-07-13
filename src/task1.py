def task1_hw2():
    # Напишите программу, которая считает общую цену.
    # Вводится M рублей и N копеек
    # цена, а также количество S товара Посчитайте общую
    # цену в рублях и копейках за L # товаров.
    # Пример:
    # Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    # Output: Общая цена 9 рублей 60 копеек

    m = int(input("Введите стоимость. Рублей: "))
    n = int(input("Введите стоимость. Копеек: "))
    s = int(input("Введите количество товаров, шт.: "))

    # переводим в стоимость всех товаров в копейки
    sum_all_prod = (n + 100 * m) * s
    # расчет и вывод стоимости
    print("Общая цена", sum_all_prod // 100, "рублей",
          sum_all_prod % 100, "копеек")


def task2_hw2():
    # Найти самое длинное слово в введенном предложении.
    # Учтите что в предложении
    # есть знаки препинания.
    # Подсказки:
    # - my_string.split([chars]) возвращает список строк.
    # - len(list) - количество элементов в списке
    # Задачу поместите в файл task2.py в папке src/homework2.

    findMax = (input("Enter your sentence:"))
    without_symbols = findMax.replace("(" or "(" or "-" or "." or ",", "")
    word = ''
    calc = ''
    for i in without_symbols:
        if i == ' ':
            if len(calc) > len(word):
                word = calc
            calc = ''
        else:
            calc += i
    print(word)


def task3_hw2():
    # Вводится строка. Требуется удалить из нее
    # повторяющиеся символы и все пробелы.
    # Например, если было введено "abc cde def",
    # то должно быть выведено "abcdef".

    str_first = input("Input string, please: ")
    str_new = ''
    for liter in str_first:
        if liter not in str_new and liter != ' ':
            str_new += liter
    print(str_new)


def task4_hw2():
    # Посчитать количество строчных (маленьких)
    # и прописных (больших) букв в
    # введенной строке. Учитывать только английские буквы.
    # Задачу поместите в файл task4.py в папке src/homework2.

    text = str(input("InPuT StRiNg: "))
    up = 0
    low = 0
    for i in text:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    print("Количество прописных букв:", up)
    print("Количество строчных букв:", low)


def task5_hw2():
    # Выведите n-ое число Фибоначчи, используя только временные переменные,
    # циклические операторы и условные операторы. n - вводится

    position = int(input("Input position number in Fibonacci row: "))
    list_Fibonacci = [0, 1]
    if position <= len(list_Fibonacci):
        print(list_Fibonacci[position - 1])
    else:
        i = 2
        while i <= position - 1:
            new_pos = list_Fibonacci[i - 2] + list_Fibonacci[i - 1]
            if i == position - 1:
                print(new_pos)
            else:
                list_Fibonacci.append(new_pos)
            i += 1


def task6_hw2():
    # Определите, является ли число палиндромом (читается
    # слева направо и справа # налево одинаково).
    # Число положительное целое, произвольной длины.
    # Задача # требует работать только с числами
    # (без конвертации числа в строку или что-нибудь еще)

    num = input("Input number to analyse palindrom it or not: ")
    len_num = len(num)
    num = int(num)
    if num == 0:
        print(0)
    else:
        x = 1
        while x <= len_num // 2:
            if x == 1:
                if num // (10 ** (len_num - x)) == num % (10 ** x) // \
                        (10 ** (x - 1)):
                    text = "It is!"
                else:
                    text = "Not, it isn't"
                    break
            else:
                if num // (10 ** (len_num - x)) % 10 == \
                        num % (10 ** x) // (10 ** (x - 1)):
                    text = "It is!"
                else:
                    text = "Not, it isn't"
                    break
            x += 1
        print(text)


def task7_hw2():
    # Даны: три стороны треугольника. Требуется: проверить,
    # действительно ли это
    # стороны треугольника. Если стороны определяют треугольник,
    # найти его площадь.
    # Если нет, вывести сообщение о неверных данных.

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        square = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        print(round(square, 3))
    else:
        print("Ошибка: неверные данные")


def task8_1_hw2():
    # Some numbers have funny properties. For example:
    # 89 --> 8¹ + 9² = 89 * 1
    # 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    # 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
    # Given a positive integer n written as abcd...
    # (a, b, c, d... being digits) and a positive integer p
    # we want to find a positive integer k, if it exists,
    # such as the sum of the digits of n taken to the successive
    # powers of p is equal to k * n.
    # In other words:
    # Is there an integer k such as : (a ^ p + b ^ (p+1)
    # + c ^(p+2) + d ^ (p+3) + ...) = n * k
    # If it is the case we will return k, if not return -1.
    # Note: n and p will always be given as strictly positive
    # integers.

    def dig_pow(n, p):
        n_len = len(str(n))
        x = 1
        num = 0
        all_num = 0
        z = 0
        while x <= n_len:
            z += num * 10 ** (n_len - x + 1)
            num = (n - z) // (10 ** (n_len - x))
            num_p = num ** (p + x - 1)
            all_num += num_p
            x += 1
        k = (all_num / n)
        if k * 10 % 10:
            return -1
        else:
            return k

    print(dig_pow(46288, 3))


def task8_2_hw2():
    # Take 2 strings s1 and s2 including only letters from ato z.
    # Return a new sorted string, the longest possible,
    # containing distinct letters - each taken only once -
    # coming from s1 or s2.
    # Examples:
    # a = "xyaabbbccccdefww"
    # b = "xxxxyyyyabklmopq"
    # longest(a, b) -> "abcdefklmopqwxy"
    # a = "abcdefghijklmnopqrstuvwxyz"
    # longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

    def longest(a1, a2):
        a1 = a1 + a2
        str_new = ''
        for lit in a1:
            if lit not in str_new and lit != ' ':
                str_new += lit
        str_sorted = "".join(sorted(str_new))
        return str_sorted

    print(longest("aretheyhere", "yestheyarehere"))


def task8_3_hw2():
    # You probably know the "like" system from Facebook
    # and other pages. People
    # can "like" blog posts, pictures or other items.
    # We want to create the
    # text that should be displayed next to such an item.
    # Implement a function likes :: [String] ->
    # String, which must take in input
    # array, containing the names of people who like an item.
    # It must return the
    # display text as shown in the examples:
    # likes([]) # must be "no one likes this"
    # likes(["Peter"]) # must be "Peter likes this"
    # likes(["Jacob", "Alex"]) # must be "Jacob and A
    # lex like this"
    # likes(["Max", "John", "Mark"]) # must be "Max,
    # John and Mark like this"
    # likes(["Alex", "Jacob", "Mark", "Max"]) # must
    # be "Alex, Jacob and 2 others

    def likes(names):
        if len(names) == 0:
            text = "no one likes this"
        elif len(names) == 1:
            name = str(names[0])
            text = str(name, "likes this")
        elif len(names) == 2:
            name = str(names[0] + " add" + names[1])
            text = str(name + " like this")
        elif len(names) == 3:
            name = str(names[0] + ", " + names[1] + " and " + names[2])
            text = str(name + " like this")
        else:
            name = str(names[0] + ", " + names[1])
            x = len(names) - 2
            text = str(name + " and " + str(x) + " others like this")
        return text

    print(likes(["Alex", "Jacob", "Mark", "Max"]))


def task8_4_hw2():
    # Usually when you buy something, you're asked whether your
    # credit card number, phone number or answer to your most
    # secret question is still correct. However, since someone
    # could look over your shoulder, you don't want that shown
    # on your screen. Instead, we mask it.
    # Your task is to write a function maskify, which changes all
    # but the last four characters into '#'.
    # Examples
    # maskify("4556364607935616") == "############5616"
    # maskify(     "64607935616") ==      "#######5616"
    # maskify(               "1") ==                "1"
    # maskify(                "") ==                 ""
    # "What was the name of your first pet?"
    # maskify("Skippy") == "##ippy"
    # maskify("Nananananananananananananananana Batman!") ==
    # "####################################man!"

    def maskify(cc):
        if 0 < len(str(cc)) <= 4:
            text = cc
        elif not len(str(cc)):
            text = ""
        else:
            j = len(str(cc)) - 4
            cc_str = str(cc)
            text = str('#' * j) + cc_str[j:]
        return text

    print(maskify(123))


def task8_5_hw2():
    #   7 kyu
    # Highest and Lowest

    # In this little assignment you are given a string of
    # space separated numbers, and have to return the
    # highest and lowest number.
    # Example:
    # high_and_low("1 2 3 4 5")  # return "5 1"
    # high_and_low("1 2 -3 4 5") # return "5 -3"
    # high_and_low("1 9 3 4 -5") # return "9 -5"
    # Notes:
    # All numbers are valid Int32, no need to validate them.
    # There will always be at least one number in the input string.
    # Output string must be two numbers separated by a single space,
    # and highest number is first.

    def high_and_low(numbers):
        len_num = len(numbers)
        num_new = []
        i = 0
        while i < len_num:
            num_int = ''
            a = numbers[i]
            while '0' <= a <= '9':
                num_int += a
                i += 1
                if i < len_num:
                    a = numbers[i]
                else:
                    break
            i += 1
            if num_int != '':
                num_new.append(int(num_int))
        numbers = str(max(num_new)) + " " + str(min(num_new))
        return numbers

    print(high_and_low("1 2 3 4 5"))


def task1_hw3():
    # Напишите программу, которая печатает цифры от 1 до 100,
    # но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
    # 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

    i = 1
    while i <= 100:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1


def task2_hw3():
    import copy

    # List practice
    # Используйте генератор списков чтобы получить
    # следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    lst_f_l = "ab"
    lst_s_l = "bcd"
    list_gen = [f_l + s_l for f_l in lst_f_l for s_l in lst_s_l]
    print(list_gen)

    # Используйте на предыдущий список slice чтобы
    # получить следующий: ['ab', 'ad', 'bc'].
    sliced_list = list_gen[::2]
    print(sliced_list)

    # Используйте генератор списков чтобы получить
    # следующий ['1a', '2a', '3a', '4a'].
    list_num_and_a = [str(num) + "a" for num in range(1, 5)]
    print(list_num_and_a)

    # Одной строкой удалите элемент  '2a' из прошлого
    # списка и напечатайте его.
    print(list_num_and_a.pop(1))

    # Скопируйте список и добавьте в него элемент
    # '2a' так чтобы в исходном списке этого элемента не было.
    new_list = copy.deepcopy(list_num_and_a)
    new_list.append("2a")
    print(new_list)


def task3_hw3():
    # Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    list_abc = ['a', 'b', 'c']
    tuple_of_list_abc = tuple(list_abc)
    print(tuple_of_list_abc)

    # Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    tuple_abc = ('a', 'b', 'c')
    list_of_tuple_abc = list(tuple_abc)
    print(list_of_tuple_abc)

    # Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    # Создайте кортеж из одного элемента, чтобы при итерировании по этому
    # элементы последовательно выводились значения 1, 2, 3.
    # Убедитесь что len() исходного кортежа возвращает 1.
    tuple_one_el = ([1, 2, 3],)
    for element in tuple_one_el[0]:
        print(element)
    print(len(tuple_one_el))


def task4_hw3():
    # Дан список чисел. Посчитайте, сколько в нем пар элементов,
    # равных друг другу. Считается, что любые два элемента,
    # равные друг другу образуют одну пару, которую необходимо посчитать.
    # Входные данные - строка из чисел, разделенная пробелами.
    # Выходные данные - количество пар.
    # Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

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
    # Дан список. Выведите те его элементы, которые встречаются в списке
    # только один раз. Элементы нужно выводить в том порядке, в котором
    # они встречаются в списке.

    list_num = [0, 1, 3, 5, 7, 2, 3, 1, 2, 1]
    list_num_new = []

    for element in list_num:
        if list_num.count(element) == 1:
            list_num_new.append(element)
    print(list_num_new)


def task6_hw3():
    # Дан список целых чисел. Требуется переместить все ненулевые
    # элементы в левую часть списка, не меняя их порядок, а все
    # нули - в правую часть. Порядок ненулевых элементов изменять
    # нельзя, дополнительный список использовать нельзя, задачу н
    # ужно выполнить за один проход по списку. Распечатайте
    # полученный список.

    list_num = [0, 1, 0, 2, 0, 3, 4, 5, 6]
    cal = 0
    x = list_num.count(0)
    while cal < x:
        list_num.append(list_num[list_num.index(0)])
        list_num.remove(0)
        cal += 1
    print(list_num)


def task1_hw4():
    # Создайте словарь с помощью генератора словарей,
    # так чтобы его ключами были числа от 1 до 20,
    # а значениями кубы этих чисел.

    dict_cube = {key: key ** 3 for key in range(1, 21)}
    print(dict_cube)


def task2_hw4():
    # Дан список стран и городов каждой страны.
    # Затем даны названия городов.
    # Для каждого города укажите, в какой стране он находится.
    # Входные данные
    # Программа получает на вход количество стран N.
    # Далее идет N строк, каждая строка начинается с названия
    # страны, затем идут названия городов этой страны. В следующей
    # строке записано число M, далее идут M запросов — названия каких-то
    # M городов, перечисленных выше.
    # Выходные данные
    # Для каждого из запроса выведите название страны, в котором находится
    # данный город.

    num_countries = int(input("Введите количество стран: "))
    country_cities_input = []
    cities_input = []
    for num_of_str in range(num_countries):
        str_country_city = input("Введите страну и города:").split()
        country_cities_input.append(str_country_city)

    num_cities = int(input("Введите количество городов: "))
    for every_city in range(num_cities):
        str_str_city = input("Введите город:").split()
        cities_input.append(str_str_city)

    for city in cities_input:
        for country_city in country_cities_input:
            if city[0] in country_city:
                print(country_city[0])


def task3_hw4():
    # Даны два списка чисел. Посчитайте, сколько различных чисел
    # содержится одновременно как в первом списке, так и во втором

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
    # Даны два списка чисел. Посчитайте, сколько различных чисел
    # содержится одновременно как в первом списке, так и во втором

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
    # Каждый из N школьников некоторой школы знает Mi языков.
    # Определите, какие языки знают все школьники и языки,
    # которые знает хотя бы один из школьников.

    pupil1_langs = ['Russian', 'English']
    pupil2_langs = ['Russian', 'Belarusian', 'English']
    pupil3_langs = ['Russian', 'Italian', 'French']
    pupil_all_langs = set(pupil1_langs + pupil2_langs + pupil3_langs)
    print("Языки, которые знают ученики: ")
    for langs in pupil_all_langs:
        print(langs)
    set_p1 = set(pupil1_langs)
    set_p2 = set(pupil2_langs)
    set_p3 = set(pupil3_langs)
    one_more_lang = set_p1 & set_p2 & set_p3
    print("Языки, которые знает хотя бы один из школьников: ")
    for lang in one_more_lang:
        print(lang)


def task6_hw4():
    # Во входной строке записан текст. Словом считается последовательность
    # непробельных символов идущих подряд, слова разделены одним или
    # большим числом пробелов или символами конца строки. Определите,
    # сколько различных слов содержится в этом тексте.

    input_text = "Текст написан и с пробелом одним и  двумя пробелами!"
    splitted_text = input_text.split()
    lst_of_unique_words = []
    for word in splitted_text:
        if word not in lst_of_unique_words:
            lst_of_unique_words.append(word)
    num_of_dif_words = len(lst_of_unique_words)
    print(num_of_dif_words)


def task7_hw4():
    # Даны два натуральных числа. Вычислите их наибольший общий делитель
    # при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))

    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    NOD = first_num + second_num
    print(NOD)


def runner(*args):
    task1_hw2()
    task2_hw2()
    task3_hw2()
    task4_hw2()
    task5_hw2()
    task6_hw2()
    task7_hw2()
    task8_1_hw2()
    task8_2_hw2()
    task8_3_hw2()
    task8_4_hw2()
    task8_5_hw2()
    task1_hw3()
    task2_hw3()
    task3_hw3()
    task4_hw3()
    task5_hw3()
    task6_hw3()
    task1_hw4()
    task2_hw4()
    task3_hw4()
    task4_hw4()
    task5_hw4()
    task6_hw4()
    task7_hw4()


runner()
