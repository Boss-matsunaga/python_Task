# 変換されたか確認
with open("hightemp.txt", "r") as f:
    txt = f.read()
    print(txt.replace("\t", "tt"))

with open("hightemp2.txt", "r") as f:
    txt2 = f.read()
    print(txt2.replace("\t", "tt"))
