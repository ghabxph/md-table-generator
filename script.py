#!/usr/env python3

import sys
from src.tablecreator import TableCreator

row = int(sys.argv[1])
col = int(sys.argv[2])
size = int(sys.argv[3])

print(TableCreator(sys.argv[1], sys.argv[2], sys.argv[3]).create_table().to_string())
