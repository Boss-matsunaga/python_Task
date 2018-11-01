def cipher(text):
    text2 = ""
    for i in text:
        if 97 <= ord(i) <= 122:
            text2+=chr(219-ord(i))
        else:
            text2+=i
    return text2


if __name__ == "__main__":
    print(cipher("HeLlO wOrLd"))