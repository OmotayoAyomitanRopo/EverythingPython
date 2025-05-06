#!/usr/bin/env python
import os # Will help chech if the file path exist in the Operating system
import sys #this provide access to command line

# import a function that load python onject from a JSON file
load_from_json_file = __import__('load_from_json').load_from_json_file

# Import a function that saves a python object to a file in JSON format
save_to_json_file = __import__('objfile').save_to_json_file

#The filename to store the list created
filename = "add_item.json"

# If a file has been created and exist load the content of the file to item
if os.path.exists(filename):
    items = load_from_json_file(filename)

# Else create this item []
else:
    items = []

# add each argument to a list
items.extend(sys.argv[1:])

# Keeps adding updated item to the file
save_to_json_file(items, filename)
