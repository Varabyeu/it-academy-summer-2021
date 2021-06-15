findMax = (input("Enter your word:"))
without_symbols = findMax.replace("(" or "(" or "-" or "." or ",", "")
li = list(without_symbols.split())
listed_li = []
for i in li:
    listed_li.append(len(i))
index_max = listed_li.index(max(listed_li))
print(li[index_max])
