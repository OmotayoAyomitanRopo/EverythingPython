#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
   sys.exit(1)

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print(f"{total}")
except ValueError:
    print("Error")
