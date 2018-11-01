text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

text2 = text.split(" ")
for i in text2:
    hoge = ""
    if len(i) <= 4:
        continue
    hoge += i[0]
    hoge += i[len(i)-1]
    print(hoge)