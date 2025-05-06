#!/usr/bin/env python
import os
import sys

load_from_json_file = __import__('load_from_json').load_from_json_file
save_to_json_file = __import__('objfile').save_to_json_file

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
