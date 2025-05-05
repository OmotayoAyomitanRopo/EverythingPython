#!/usr/bin/env python3
def append_write(filename="", text=""):
    with open("file_append.txt", "a", encoding="utf8") as file:
        return file.write(text)
