#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    a = sys.argv
    b = len(a) - 1

    if b > 1:
        print(b, "arguments:")
        for i in range(1, b + 1):
            print("{:d}: {}".format(i, a[i]))
    elif b == 1:
        print(b, "arguments:")
        for i in range(1, b + 1):
            print("{:d}: {}".format(i, a[i]))
    elif b == 0:
        print(b, "arguments.")
