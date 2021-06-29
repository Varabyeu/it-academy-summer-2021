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
print("В первом списке количество различных чисел - {}.".format(count_unicl_numbrs_frst))
print("Во втором списке количество различных чисел - {}.".format(count_unicl_numbrs_scnd))
