#!/usr/bin/env python
import json
def load_from_json_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        return json.load(f)
