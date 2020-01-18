import random
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

text2 = text.split(" ")
for i in text2:
    result = ""
    hoge = ""
    hoge2 = ""
    j = ""
    k = []
    if len(i) <= 4:
        continue
    hoge += i[0]
    hoge2 += i[len(i)-1]
    j = i[1:len(i)-1]
    k = [jj for jj in j]
    #print(k)
    random.shuffle(k)
    result += (hoge+''.join(k)+hoge2)
    print(result)