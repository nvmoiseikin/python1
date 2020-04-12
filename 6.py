import re

school_dict = {}
with open("6.txt", mode="rt", encoding="utf-8") as file:
    for line in file.readlines():
        data = [0 if lessons == "—" else lessons for lessons in re.findall(r"(\d+|—)", line)]
        sum_lessons = sum(map(int, data))
        lesson_name = re.findall(r"(\w+):", line)[0]
        school_dict[lesson_name] = sum_lessons
print(school_dict)