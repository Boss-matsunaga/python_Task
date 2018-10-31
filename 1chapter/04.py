text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dic = {}
count = 1
li = [1, 5, 6, 7, 8, 9, 15, 16, 19]
flag = 1

for i in text:
    mo = ""
    if i == " " or i == ".":
        count += 1
        flag = 1
    elif count in li and flag == 1:
        flag = 0
        mo += i
        # mo += i+1
        dic[mo] = count
    elif flag == 1:
        flag = 0
        mo += i
        dic[mo] = count

print(dic)