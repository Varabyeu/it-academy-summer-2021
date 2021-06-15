a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** (1 / 2))
else:
    print("Ошибка: неверные данные")
