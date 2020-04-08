from itertools import count
import sys

try:
    if "help" in sys.argv:
        print("This script generate positive integer start from first param")
    else:
        start = int(sys.argv[1])
        for i in count(start):
            print(i)
            if i > 100:
                break
except ValueError as e:
    print(f"Error! {e}, run with param 'help'")
