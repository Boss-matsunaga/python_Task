import ngram

text = "I am an NLPer"

def ngram(n):
    text2 = ngram.NGram(n)
    for i in index.ngrams(index.pad(text)):
        print(i)

if __name__ == '__main__':
    ngram(4)