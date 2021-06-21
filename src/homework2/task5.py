position = int(input())
list_Fibonacci = [0, 1]
if position <= len(list_Fibonacci):
    print(list_Fibonacci[position - 1])
else:
    i = 2
    while i <= position - 1:
        new_pos = list_Fibonacci[i - 2] + list_Fibonacci[i - 1]
        if i == position - 1:
            print(new_pos)
        else:
            list_Fibonacci.append(new_pos)
        i += 1
