# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
# 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz


i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1
