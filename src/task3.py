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
tuple_one_el = ([1, 2, 3], )
for element in tuple_one_el[0]:
    print(element)
print(len(tuple_one_el))

