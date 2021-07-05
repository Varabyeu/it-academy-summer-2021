"""Языки.
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник, на следующих
строках - список таких языков.
"""
# Указываем количество учеников
student_counter = 3
# Входные данные
first_student = ['Rus', 'Bel']
second_student = ['Rus', 'Bel', 'Eng']
third_student = ['Rus', 'Itl', 'Fr']
# Определяем язык(и) которые знают все
popular_lang = set(
    first_student) & set(second_student) & set(third_student)
print(len(popular_lang))
print('Все знают ---> ', list(popular_lang))
# Определяем языки которые знает хотя бы один ученик
lang_list = set(
    first_student) | set(second_student) | set(third_student)
print(len(lang_list))
print('Эти языки знает хотя бы один ученик ---> ', list(lang_list))