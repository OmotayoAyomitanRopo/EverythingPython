#!/usr/bin/env python
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
