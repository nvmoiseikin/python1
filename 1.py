import sys

try:
    if "help" in sys.argv:
        print("This script calculate the salary.",
              "First papram is amount of worker hours.",
              "Second param is money in dollar per hour.",
              "Third param is month bonus in dollar.", sep="\n")
    else:
        hours, dollars_per_hour, month_bonus = map(int, sys.argv[1:])
        print(f"salary = {(hours * dollars_per_hour) + month_bonus}")
except ValueError as e:
    print(f"Error! {e}, run with param 'help'")