#!/usr/bin/env python
def write_file(filename="", text=""):
    with open("my_first_file.txt", "w", encoding="utf8") as f:
        return f.write("txt")
