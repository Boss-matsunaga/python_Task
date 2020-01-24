import re


def main():
    ans_dict = {}
    with open("jawiki-uk.txt", "r") as f:
        uk_data = f.read().split("\n")
    for line in uk_data:
        if re.search(r"^[|].*\s=", line):
            tmp = line.split(" = ")
            ans_dict[tmp[0][1:]] = tmp[1]
    print(ans_dict)


if __name__ == "__main__":
    main()
