str_first = input()
str_new = ''
for litera in str_first:
    if litera not in str_new and litera != ' ':
        str_new += litera
print(str_new)
