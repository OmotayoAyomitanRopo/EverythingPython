#!/usr/bin/env python
Student = __import__('9-student').Student

students = [Student("john", "doe", 13), Student("Bob", "Ayo", 45)]

for student in students:
    j = student.to_json()
    print(type(j))
    print(j)
    print(j['first_name'])
    print(j['last_name'])
    print(j['age'])
