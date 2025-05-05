#!/usr/bin/env python
append_write = __import__('append').append_write

nb_characters_added = append_write("file_append.txt", "this is cool")
print(nb_characters_added)
