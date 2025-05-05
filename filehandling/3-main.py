#!/usr/bin/env python 
to_json_string = __import__('jsonstring').to_json_string

my_list = [1, 2, 3, 4, 5]
nlist = to_json_string(my_list)
print(nlist)
print(type(nlist))

my_obj = {
        'id': 12,
        'name': "john",
        'places': ["san franscisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'avaerage': 3.24
    }
}
nobj = to_json_string(my_obj)
print(nobj)
print(type(nobj))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
