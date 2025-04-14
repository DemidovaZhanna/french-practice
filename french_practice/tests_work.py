def get_tests():    # Парсинг tests.csv
    tests = []
    with open("./data/tests.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for i, line in enumerate(lines, 1):
            parts = line.strip().split(";")
            if len(parts) < 2:
                continue
            text, country = parts[:2]
            tests.append((i, text, country))
    return tests
