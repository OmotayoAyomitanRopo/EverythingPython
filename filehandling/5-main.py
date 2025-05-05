#!/usr/bin/env python 
save_to_json_file = __import__('objfile').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3, 4, 5]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
        'id': 12,
        'name': "john",
        'places': ["san franscisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'avaerage': 3.24
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
