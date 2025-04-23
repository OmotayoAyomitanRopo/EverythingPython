#!/usr/bin/env python
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    for char in ".,?:":
        text = text.replace(char, char + "\n\n")

    for line in text.split("\n"):
        print(line.strip())
