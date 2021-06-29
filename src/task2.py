# Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия
# страны, затем идут названия городов этой страны. В следующей
# строке записано число M, далее идут M запросов — названия каких-то
# M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится
# данный город.

num_countries = int(input("Введите количество стран: "))
calc = 0
country_cities_input = []
cities_input = []
for num_of_str in range(num_countries):
    str_country_city = input("Введите страну и города:").split()
    country_cities_input.append(str_country_city)

num_cities = int(input("Введите количество городов: "))
for every_city in range(num_cities):
    str_str_city = input("Введите город:").split()
    cities_input.append(str_str_city)

for city in cities_input:
    for country_city in country_cities_input:
        if city[0] in country_city:
            print(country_city[0])
