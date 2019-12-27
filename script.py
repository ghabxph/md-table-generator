#!/usr/env python3

import sys

row = int(sys.argv[1])
col = int(sys.argv[2])
size = int(sys.argv[3])

# The header part
table = "|"
for y in range(col):
    for z in range(size):
        table = table + " "
    table = table + "|"
table = table + "\n"

# The separator from header and regular data
table = table + "|"
for y in range(col):
    for z in range(size):
        table = table + "-"
    table = table + "|"
table = table + "\n"

# The data part (applies row)
for x in range(row):
    table = table + "|"
    for y in range(col):
        for z in range(size):
            table = table + " "
        table = table + "|"
    table = table + "\n"

print(table)