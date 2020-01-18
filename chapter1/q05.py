text = "I am an NLPer"

def moz_ngram(n):
    text2 = text.replace(" ", "")
    for i in range(0, len(text2), n-1):
        result1 = ""
        result1 += text2[i:i+n]
        print(result1)

def tan_ngram(n):
    text2 = text.split(" ")
    for i in range(0, len(text2), n-1):
        k = ""
        result2 = []
        result2 += text2[i:i+n]
        k = ''.join(result2)
        print(k)

if __name__ == '__main__':
    tan_ngram(2)
    moz_ngram(2)