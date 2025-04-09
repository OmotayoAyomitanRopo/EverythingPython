#!/usr/bin/env python
import sys
arglen = len(sys.argv) - 1
print(f"total arg: {arglen}")
for indx, arg in enumerate(sys.argv[1: ], start=1):
    print(f"{indx}: {arg}")


