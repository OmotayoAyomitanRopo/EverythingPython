#!/usr/bin/env python
Base = __import__('base').Base

b1 = Base(12)
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base()
print(b3.id)

b4 = Base()
print(b4.id)
