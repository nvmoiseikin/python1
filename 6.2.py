from itertools import cycle
import sys

my_list = [1, 2, 3, 4, 5]
try:
    if "help" in sys.argv:
        print("This script cycle the elements of my_list ")
    else:
        for i, el in enumerate(cycle(my_list)):
            print(el)
            if i > 100:
                break
except ValueError as e:
    print(f"Error! {e}, run with param 'help'")