m = int(input("Введите стоимость. Рублей:"))
n = int(input("Введите стоимость. Копеек:"))
s = int(input("Введите количество товаров, шт.:"))

# переводим в стоимость всех товаров в копейки
sum_all_prod = (n + 100 * m) * s
# расчет и вывод стоимости
print("Общая цена", sum_all_prod // 100, "рублей", sum_all_prod % 100, "копеек")
