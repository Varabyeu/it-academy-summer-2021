"""

Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия
 страны, затем идут названия городов этой страны. В следующей
 строке записано число M, далее идут M запросов — названия каких-то
 M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город.

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa


3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia

"""

# num_countries = int(input("Введите количество стран: "))
# calc = 0
# country_cities_input = []
# cities_input = []
# for num_of_str in range(num_countries):
#     str_country_city = input("Введите страну и города:").split()
#     country_cities_input.append(str_country_city)
#
# num_cities = int(input("Введите количество городов: "))
# for every_city in range(num_cities):
#     str_str_city = input("Введите город:").split()
#     cities_input.append(str_str_city)
#
# for city in cities_input:
#     for country_city in country_cities_input:
#         if city[0] in country_city:
#             print(country_city[0])


num_countries = int(input("Введите количество стран: "))
every_country = 1
dict_cities_in_countries = {}
while every_country <= num_countries:
    name_country_city = list(input("Введите страну и города №{}: ".format(every_country)).split())
    country = name_country_city[0]
    dict_country_city = {country: name_country_city[1::]}
    dict_cities_in_countries.update(dict_country_city)
    every_country += 1
num_cities = int(input("Введите количество городов: "))
every_city = 1
list_countries = []
while every_city <= num_cities:
    searching_cities = input("Введите название города №{}: ".format(every_city)).split()
    for searching_city in searching_cities:
        for searching_country, cities in dict_cities_in_countries.items():
            if searching_city in cities:
                list_countries.append(searching_country)
    every_city += 1
for country in list_countries:
    print(country)
