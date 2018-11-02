result = ""
text2 = text.split(" ")
print(text2)
for i in range(0, len(text2), n-1):
    result2 = []
    result2 += text2[i:i+n]

    for j in result2:
        result += j
    print(result)