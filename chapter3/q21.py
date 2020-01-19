def main():
    with open("jawiki-uk.txt", "r") as f:
        uk_data = f.read().split("\n")
    for line in uk_data:
        if "Category" not in line:
            continue
        print(line)


if __name__=="__main__":
    main()