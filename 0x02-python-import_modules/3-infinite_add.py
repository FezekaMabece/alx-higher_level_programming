#!/usr/bin/python3
import sys

if __name__ == "__main__":
    a = sys.argv
    b = len(a)
    sum = 0
    if b > 1:
        for i in range(1, b):
            sum += int(a[i])

    print(sum)
