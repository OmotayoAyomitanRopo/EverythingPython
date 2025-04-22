#!/usr/bin/env python
Rectangle = __import__('4-Rectanle').Rectangle



My_rec = Rectangle(2, 4)

print(My_rec)
print('_____')
print(str(My_rec))
print("_____")
print(repr(My_rec))
print("____")
print(hex(id(My_rec)))



# Create new instance based on repr

New_rec = eval(repr(My_rec))
print(New_rec)
print('_____')
print(str(New_rec))
print("_____")
print(repr(New_rec))
print("____")
print(hex(id(New_rec)))

print(New_rec is My_rec)
print(type(New_rec) is type(My_rec))

