"""

Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или
большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.

"""

input_text = "Текст написан и с (пробелом) одним и  двумя! пробелами?..."

for symbol in ("!", ".", "?", "...", "(", ")"):
    input_text = input_text.replace(symbol, "")
splitted_text = input_text.split()
print(input_text)
lst_of_unique_words = []
for word in splitted_text:
    if word not in lst_of_unique_words:
        lst_of_unique_words.append(word)
num_of_dif_words = len(lst_of_unique_words)
print(num_of_dif_words)
