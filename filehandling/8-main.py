#!/usr/bin/env python
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('class_to_json').class_to_json

m = MyClass("Ayor")
m.number = 90

print(m)
print(type(m))

mj = class_to_json(m)
print(mj)
print(type(mj))
