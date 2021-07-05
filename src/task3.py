"""

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
