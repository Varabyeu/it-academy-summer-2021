import copy

# List practice
# Используйте генератор списков чтобы получить
# следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list_first_lit = "ab"
list_second_lit = "bcd"
list_gen = [frst_lit + sec_lit for first_lit in list_first_lit for sec_lit in list_scnd_lit]

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
