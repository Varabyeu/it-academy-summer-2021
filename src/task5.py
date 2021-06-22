# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.


list_num = [0, 1, 3, 5, 7, 2, 3, 1, 2, 1]
list_num_new = []


for element in list_num:
    if list_num.count(element) == 1:
        list_num_new.append(element)
print(list_num_new)
