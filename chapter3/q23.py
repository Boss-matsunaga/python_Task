import re


def main():
    with open("jawiki-uk.txt", "r") as f:
        uk_data = f.read().split("\n")
    for line in uk_data:
        if re.search(r"={4}", line):
            print("    3", re.sub(r"[=\s]", "", line))
        elif re.search(r"={3}", line):
            print("  2", re.sub(r"[=\s]", "", line))
        elif re.search(r"={2}", line):
            print("1", re.sub(r"[=\s]", "", line))


if __name__ == "__main__":
    main()
