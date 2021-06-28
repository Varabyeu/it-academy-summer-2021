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
