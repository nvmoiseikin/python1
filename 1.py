with open("1.txt", mode="w", encoding="utf-8") as file:
    while True:
        line = input("введите строку ")
        if line == "":
            break
        file.write(line + "\n")
