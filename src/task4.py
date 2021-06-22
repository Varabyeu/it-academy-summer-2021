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
