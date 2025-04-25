#!/usr/bin/env python
MyList = __import__('Mylistclass').MyList

mylist = MyList()

mylist.append(3)
mylist.append(2)
mylist.append(4)
mylist.append(1)
print(mylist)
print(mylist.print_sorted())
