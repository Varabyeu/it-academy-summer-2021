Num = input()
len_num = len(Num)
Num = int(Num)
if Num == 0:
    print(0)
else:
    x = 1
    while x <= len_num // 2:
        if x == 1:
            if Num // (10**(len_num - x)) == Num % (10**x) // (10**(x - 1)):
                text = "Пара"
            else:
                text = "Не"
                break
        else:
            if Num // (10**(len_num - x)) % 10 == \
                    Num % (10**x) // (10**(x - 1)):
                text = "Пара"
            else:
                text = "Не"
                break
        x += 1
    print(text)

