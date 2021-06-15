listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []
for item in listOrigin:
    if item > 0:
        listMask.append(1)
    elif item < 0:
        listMask.append(-1)
    else:
        listMask.append(0)

print(listOrigin)
print(listMask)