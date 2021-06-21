num = input()
len_num = len(num)
num = int(num)
if num == 0:
    print(0)
else:
    x = 1
    while x <= len_num // 2:
        if x == 1:
            if num // (10**(len_num - x)) == num % (10**x) // (10**(x - 1)):
                text = "Пара"
            else:
                text = "Не"
                break
        else:
            if num // (10**(len_num - x)) % 10 == \
                    num % (10**x) // (10**(x - 1)):
                text = "Пара"
            else:
                text = "Не"
                break
        x += 1
    print(text)
