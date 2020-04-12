import json
companies = {}

with open("7.in.txt", mode="rt", encoding="utf-8") as file:
    for line in file.readlines():
        name, type_com, profit, costs = line.split(" ")
        companies[name] = int(profit) - int(costs)

com_in_plus = [profit for profit in companies.values() if profit >= 0]
com_stats = json.dumps([companies, {"average_profit": sum(com_in_plus)//len(com_in_plus)}])
#Знаю что есть json.dump(), так вроде структура логичнее.

with open("7.out.txt", mode="wt", encoding="utf-8") as file:
    file.write(com_stats)
