#!/usr/bin/env python
say_my_name = __import__('name').say_my_name

say_my_name("Ayomitan", "Omotayo")
say_my_name("Ayor")
try:
    say_my_name(84, "ayo")
except Exception as e:
    print(e)
