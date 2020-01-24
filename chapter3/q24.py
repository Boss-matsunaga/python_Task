import re


def main():
    with open("jawiki-uk.txt", "r") as f:
        uk_data = f.read().split("\n")
    for line in uk_data:
        if "ファイル" not in line and "File" not in line:
            continue
        matchstr = re.search(
            r"^[A-Za-z0-9\s-]*[.](jpg|svg|JPG)", line.split(":")[1])
        if matchstr:
            print(matchstr.group())


if __name__ == "__main__":
    main()
