text = "I am an NLPer"

def tan_ngram(n):
    text2 = text.replace(" ", "")
    print(text2)
    for i in range(0, len(text2), n-1):
        result1 = ""
        result1 += text2[i:i+n]
        print(result1)

def moz_ngram(n):
    result = ""
    text2 = text.split(" ")
    print(text2)
    for i in range(0, len(text2), n-1):
        result2 = []
        result2 += text2[i:i+n]
        for j in result2:
            result += j
        print(j)

if __name__ == '__main__':
    tan_ngram(3)
    moz_ngram(2)