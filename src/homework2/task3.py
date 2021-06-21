# Вводится строка. Требуется удалить из нее
# повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

str_first = input()
str_new = ''
for liter in str_first:
    if liter not in str_new and liter != ' ':
        str_new += liter
print(str_new)
