#!/usr/bin/env python
for x in range(97, 123):
    if x == 99 or x == 101:
        continue
    print(chr(x), end="")
