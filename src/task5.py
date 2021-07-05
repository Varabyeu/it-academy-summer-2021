"""

Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

Пример входных данных:
3  # N количество школьников
2  # M1 количество языков первого школьника

Russian  # языки первого школьника
English

3  # M2 количество языков второго школьника
Russian
Belarusian
English

3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все
школьники. Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один
школьник, на следующих строках - список таких языков.

"""

number_of_pupils = 3
pupil1_num_lang = 2
pupil1_langs = ['Russian', 'English']
pupil2_num_lang = 3
pupil2_langs = ['Russian', 'Belarusian', 'English']
pupil3_num_lang = 3
pupil3_langs = ['Russian', 'Italian', 'French']
pupil_all_langs = set(pupil1_langs + pupil2_langs + pupil3_langs)
print("Языки, которые знает хотя бы один ученик: ")
for langs in pupil_all_langs:
    print(langs)
set_p1 = set(pupil1_langs)
set_p2 = set(pupil2_langs)
set_p3 = set(pupil3_langs)
one_more_lang = set_p1 & set_p2 & set_p3
print("Языки, которые знают все ученики: ")
for lang in one_more_lang:
    print(lang)
