text = str(input())
i = 0
j = len(text) -1
x = 0
y = 0


while i <= j:
    if ord('A') <= ord(text[i]) < ord('a'):
        x += 1
    else:
        if ord(text[i]) >= ord('a'):
            y += 1
    i += 1
print("Количество строчных букв:", x)
print("Количество прописных букв:", y)
