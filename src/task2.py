import copy

# List practice
# Используйте генератор списков чтобы получить
# следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list1 = "ab"
list2 = "bcd"
list_gen = []
for element1 in list1:
    for element2 in list2:
        list_gen.append(element1 + element2)
print(list_gen)


# Используйте на предыдущий список slice чтобы
# получить следующий: ['ab', 'ad', 'bc'].
sliced_list = list_gen[::2]
print(sliced_list)


# Используйте генератор списков чтобы получить
# следующий ['1a', '2a', '3a', '4a'].
list_wth_a = []
list_num = [1, 2, 3, 4]
for el in list_num:
    list_wth_a.append(str(el) + "a")
print(list_wth_a)


# Одной строкой удалите элемент  '2a' из прошлого
# списка и напечатайте его.
print(list_wth_a.pop(1))


# Скопируйте список и добавьте в него элемент
# '2a' так чтобы в исходном списке этого элемента не было.
new_list = copy.deepcopy(list_wth_a)
new_list.append("2a")
print(new_list)
