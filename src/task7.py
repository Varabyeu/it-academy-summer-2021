"""

Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

"""

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

while first_num != 0 and second_num != 0:
    if first_num > second_num:
        first_num = first_num % second_num
    else:
        second_num = second_num % first_num
NOD = first_num + second_num
print(NOD)
