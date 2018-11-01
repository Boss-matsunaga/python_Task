text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dic = {}
li = [1, 5, 6, 7, 8, 9, 15, 16, 19]


text2 = text.split(" ")

for i in text2:
    if (text2.index(i)+1) in li:
        dic[i[0:2]] = text2.index(i)+1
    else:
        dic[i[0]] = text2.index(i)+1

print(dic)