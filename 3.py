with open("3.txt", mode="rt", encoding="utf-8") as file:
    lines = file.readlines()
    sum_salary = 0
    for line in lines:
        try:
            name, salary = line.strip().split(" ")
            if int(salary) > 20000:
                print(f"Фамилия {name} с зарплатой {salary}")
            sum_salary += int(salary)
        except ValueError as e:
            print("Ошибка в данных файла '3.txt'")
    print(f"Средняя заплата составляет {sum_salary/len(lines):.2f}")

