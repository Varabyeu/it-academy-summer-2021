pre = 1
last = 2
pos = int(input())
if pos <= 2:
    num = pre
elif pos == 3:
    num = last
else:
    while pos - 4 >= 0:
        num = last + pre
        pre = last
        last = num
        pos -= 1
print(num)
