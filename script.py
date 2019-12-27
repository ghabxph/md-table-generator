#!/usr/env python3

import sys

row = int(sys.argv[1])
col = int(sys.argv[2])
size = int(sys.argv[3])

# The header part
print("|")
for y in range(col):
    for z in range(size):
        print(" ")
    print("|")
print("\n")

# The separator from header and regular data
print("|")
for y in range(col):
    for z in range(size):
        print("-")
    print("|")
print("\n")

# The data part (applies row)
for x in range(row):
    print("|")
    for y in range(col):
        for z in range(size):
            print(" ")
        print("|")
    print("\n")
