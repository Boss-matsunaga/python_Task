import json


def main():
    with open("jawiki-country.json", "r") as fs:
        for f in fs:
            jd = json.loads(f)
            if jd["title"] != "イギリス":
                continue
            uk_data = jd["text"]

    with open("jawiki-uk.txt", "w", encoding="utf8") as f:
        f.write(uk_data)


if __name__ == "__main__":
    main()
