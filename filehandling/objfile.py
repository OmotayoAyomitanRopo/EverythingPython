#!/usr/bin/env python
import json
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf8") as f:
        return json.dump(my_obj, f)
