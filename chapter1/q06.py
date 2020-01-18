text = "paraparaparadise"
text2 = "paragraph"
n = 2

X = []
Y = []

for i in range(0, len(text), n-1):
    result1 = ""
    result1 += text[i:i+n]
    X.append(result1)

for i in range(0, len(text2), n-1):
    result2 = ""
    result2 += text2[i:i+n]
    Y.append(result2)

if 'se' in X or 'se' in Y:
    print("ある")

# print(X)
# print(Y)

for i in X:
    for j in Y:
        ii = set(i)
        jj = set(j)
        print("和集合")
        print(ii | jj)
        print("積集合")
        print(ii & jj)
        print("差集合")
        print(ii - jj)