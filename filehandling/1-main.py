#!/usr/bin/env python
write_file = __import__('writefile').write_file

nbchar = write_file("my_first_file.txt", "this schoolis cool")
print(nbchar)
