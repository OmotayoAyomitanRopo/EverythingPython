#!/usr/bin/env python
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('readfile').read_file
save_to_json_file = __import__('objfile').save_to_json_file
load_from_json_file = __import__('load_from_json').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

s_1 = Student("John", "Doe", 34)
j_s1 = s_1.to_json()
print("initial student")
print(s_1)
print(type(s_1))
print(type(j_s1))
print("{} {} {}".format(s_1.first_name, s_1.last_name, s_1.age))

save_to_json_file(j_s1, path)
read_file(path)
print("\n saved to disk")

print("Fake student")
newS_1 = Student("Fake", "A fake", 89)
print(newS_1)
print(type(newS_1))
print("{} {} {}".format(newS_1.first_name, newS_1.last_name, newS_1.age))

print("Loading dictionary file")
new_j_s1 = load_from_json_file(path)

newS_1.reload_from_json(j_s1)
print(newS_1)
print(type(newS_1))
print("{} {} {}".format(newS_1.first_name, newS_1.last_name, newS_1.age))

