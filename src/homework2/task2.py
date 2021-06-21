# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении
# есть знаки препинания.
# Подсказки:
# - my_string.split([chars]) возвращает список строк.
# - len(list) - количество элементов в списке
# Задачу поместите в файл task2.py в папке src/homework2.

findMax = (input("Enter your sentence:"))
without_symbols = findMax.replace("(" or "(" or "-" or "." or ",", "")
word = ''
calc = ''
for i in without_symbols:
    if i == ' ':
        if len(calc) > len(word):
            word = calc
        calc = ''
    else:
        calc += i
print(word)
