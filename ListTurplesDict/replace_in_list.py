#!/usr/bin/env python
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    
    new_list = my_list[:] #store a copy of the original list
    new_list[idx] = element # creatte a new list to include the new element
    return new_list #return the newly created list
