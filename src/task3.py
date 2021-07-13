"""

Реализовать функцию get_ranges которая получает на вход непустой список
 неповторяющихся целых чисел, отсортированных по возрастанию, которая
  этот список “сворачивает”

 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(list_num):
    list_items = []
    list_temp = []
    while len(list_num):
        if len(list_num) >= 2:
            if list_num[-1] - list_num[-2] == 1:
                while list_num[-1] - list_num[-2] == 1:
                    temp_num = list_num.pop(-1)
                    list_temp.append(temp_num)
                    if len(list_num) < 2:
                        break
                temp_num = list_num.pop(-1)
                list_temp.append(temp_num)
                str_ = ''.join(str(list_temp[-1]) + '-' + str(list_temp[0]))
                list_items.append(str_)
                list_temp.clear()
            else:
                temp_num = list_num.pop(-1)
                list_items.append(temp_num)
        else:
            temp_num = list_num.pop(-1)
            str_ = ''.join(str(temp_num))
            list_items.append(str_)
    list_items.reverse()
    str_results = ''
    for element in list_items:
        if element != list_items[-1]:
            str_results += str(element) + ', '
        else:
            str_results += str(element)
    return str_results


ranges1 = [0, 1, 2, 3, 4, 7, 8, 10]
ranges2 = [4, 7, 10]
ranges3 = [2, 3, 8, 9]


print(get_ranges(ranges1))
print(get_ranges(ranges2))
print(get_ranges(ranges3))
