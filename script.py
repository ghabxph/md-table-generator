#!/usr/env python3

import sys
from src.tablecreator import TableCreator

print(TableCreator(sys.argv[1], sys.argv[2], sys.argv[3]).create_table().to_string())
