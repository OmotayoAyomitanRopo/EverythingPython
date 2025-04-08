#!/usr/bin/env python
def uppercase(str):
    result = "" # initialize an empty string stored in result
    for char in str: # oop all char in the string
        result += char.upper() # Converts all character to uppercase
    print(result)
