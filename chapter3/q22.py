import re

def main():
    with open("jawiki-uk.txt", "r") as f:
        uk_data = f.read().split("\n")
    for line in uk_data:
        if "Category" not in line:
            continue
        matchstr = re.sub(r"[\|\*\]]", "", line.split(":")[1])
        if  matchstr:
            print(matchstr)


if __name__ == "__main__":
    main()