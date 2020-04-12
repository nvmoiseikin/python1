with open("2.txt", mode="rt", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(f"Строка '{line.strip()}': количество символов {len(line.strip())}")
    print(f"Количество строк {len(lines)}")
