"""
Homework2 module with all tasks for task1 in homework5
"""


def task1_hw2(rub=2, kop=30, number=3):
    """
    Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек
    цена, а также количество S товара Посчитайте общую
    цену в рублях и копейках за L # товаров.

    Пример:
    Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    Output: Общая цена 9 рублей 60 копеек
    """

    # переводим в стоимость всех товаров в копейки
    sum_all_prod = (kop + 100 * rub) * number
    # расчет и вывод стоимости
    print("Общая цена", sum_all_prod // 100, "рублей",
          sum_all_prod % 100, "копеек")


def task2_hw2(sentence='Самое Длинное Слово В Введенном предложении'):
    """Найти самое длинное слово в введенном предложении.

    Учтите что в предложении есть знаки препинания.
    Подсказки:
    - my_string.split([chars]) возвращает список строк.
    - len(list) - количество элементов в списке
    Задачу поместите в файл task2.py в папке src/homework2.
    """

    without_symbols = sentence.replace("(" or "(" or "-" or "." or ",", "")
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


def task3_hw2(str_first='abc cde def'):
    """
    Вводится строка. Требуется удалить из нее
    повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def",
    то должно быть выведено "abcdef".
    """

    str_new = ''
    for liter in str_first:
        if liter not in str_new and liter != ' ':
            str_new += liter
    print(str_new)


def task4_hw2(text='Сколько Строчных и Прописных букв'):
    """
    Посчитать количество строчных (маленьких)
    и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
    Задачу поместите в файл task4.py в папке src/homework2.
    """

    up = 0
    low = 0
    for i in text:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    print("Количество прописных букв:", up)
    print("Количество строчных букв:", low)


def task5_hw2(position=5):
    """
    Выведите n-ое число Фибоначчи, используя только временные
    переменные, Циклические операторы и условные операторы.
    n - вводится
    """

    list_fibonacci = [0, 1]
    if position <= len(list_fibonacci):
        print(list_fibonacci[position - 1])
    else:
        i = 2
        while i <= position - 1:
            new_pos = list_fibonacci[i - 2] + list_fibonacci[i - 1]
            if i == position - 1:
                print(new_pos)
            else:
                list_fibonacci.append(new_pos)
            i += 1


def task6_hw2(number=12321):
    """Определите, является ли число палиндромом (читается
    слева направо и справа # налево одинаково).
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами
    (без конвертации числа в строку или что-нибудь еще)
    """
    num = str(number)
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


def task7_hw2(a=1, b=2, c=3):
    """
    Даны: три стороны треугольника. Требуется: проверить,
    действительно ли это
    стороны треугольника. Если стороны определяют треугольник,
    найти его площадь.
    Если нет, вывести сообщение о неверных данных.
    """

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        square = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        print(round(square, 3))
    else:
        print("Ошибка: неверные данные")


def task8_1_hw2():
    """
    Some numbers have funny properties. For example:
    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
    Given a positive integer n written as abcd...
    (a, b, c, d... being digits) and a positive integer p
    we want to find a positive integer k, if it exists,
    such as the sum of the digits of n taken to the successive
    powers of p is equal to k * n.
    In other words:
    Is there an integer k such as : (a ^ p + b ^ (p+1)
    + c ^(p+2) + d ^ (p+3) + ...) = n * k
    If it is the case we will return k, if not return -1.
    Note: n and p will always be given as strictly positive
    integers.
    """

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
    """
    Return a new sorted string, the longest possible,
    containing distinct letters - each taken only once -
    coming from s1 or s2.
    Examples:
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a, b) -> "abcdefklmopqwxy"
    a = "abcdefghijklmnopqrstuvwxyz"
    longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
    """

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
    """
    You probably know the "like" system from Facebook
    and other pages. People
    can "like" blog posts, pictures or other items.
    We want to create the
    text that should be displayed next to such an item.
    Implement a function likes :: [String] ->
    String, which must take in input
    array, containing the names of people who like an item.
    It must return the
    display text as shown in the examples:
    likes([]) # must be "no one likes this"
    likes(["Peter"]) # must be "Peter likes this"
    likes(["Jacob", "Alex"]) # must be "Jacob and A
    lex like this"
    likes(["Max", "John", "Mark"]) # must be "Max,
    John and Mark like this"
    likes(["Alex", "Jacob", "Mark", "Max"]) # must
    be "Alex, Jacob and 2 others
    """

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
    """
    Usually when you buy something, you're asked whether your
    credit card number, phone number or answer to your most
    secret question is still correct. However, since someone
    could look over your shoulder, you don't want that shown
    on your screen. Instead, we mask it.
    Your task is to write a function maskify, which changes all
    but the last four characters into '#'.
    Examples
    maskify("4556364607935616") == "############5616"
    maskify(     "64607935616") ==      "#######5616"
    maskify(               "1") ==                "1"
    maskify(                "") ==                 ""
    "What was the name of your first pet?"
    maskify("Skippy") == "##ippy"
    maskify("Nananananananananananananananana Batman!") ==
    "####################################man!"
    """

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
    """Highest and Lowest

    In this little assignment you are given a string of
    space separated numbers, and have to return the
    highest and lowest number.
    Example:
    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
    Notes:
    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space,
    and highest number is first.
    """

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
