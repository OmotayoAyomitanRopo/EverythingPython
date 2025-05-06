#!/usr/bin/env python
Student = __import__('10-student').Student

s_1 = Student("John", "dot", 34)
s_2 = Student("Ayo", "Mitan", 32)

j_1 = s_1.to_json()
j_2 = s_2.to_json(['first_name', 'age'])
j_3 = s_2.to_json(['middle_name', 'age'])

print(j_1)
print(j_2)
print(j_3)
