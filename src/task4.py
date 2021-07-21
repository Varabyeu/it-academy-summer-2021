"""

В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
 ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""

try:
    with open("ratings.list") as rating_list:
        print("")
        rating_list.seek(830)
        all_tags = []
        for line in rating_list:
            try:
                list_film_line = line.split()
                name_of_film = ''
                for elements in list_film_line[3:-1]:
                    name_of_film += str(elements) + ' '
                all_tags.append([name_of_film,
                                 list_film_line[2],
                                 line.split('(')[1][0:4]])
            except IndexError:
                break

        with open("top250_movies.txt", "w") as top250films_file:
            for el in all_tags:
                top250films_file.write(str(el[0]) + '\n')

        with open("ratings.txt", "w") as ratings_file:
            list_of_rates = []
            for tag in all_tags:
                list_of_rates.append(tag[1])
            list_of_unical_rates = sorted(list(set(list_of_rates)),
                                          reverse=True)
            for rate in list_of_unical_rates:
                count_rates = list_of_rates.count(rate)
                ratings_file.write(str(rate) + ':' + str(count_rates) + '\n')

        with open("years.txt", "w") as years_file:
            list_of_years = []
            for tag in all_tags:
                list_of_years.append(tag[2])
            list_of_unical_years = sorted(list(set(list_of_years)),
                                          reverse=True)
            for year in list_of_unical_years:
                count_years = list_of_years.count(year)
                years_file.write(str(year) + ':' + str(count_years) + '\n')
except FileNotFoundError:
    print("File lost")
