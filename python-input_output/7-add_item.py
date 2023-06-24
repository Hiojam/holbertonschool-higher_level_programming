#!/usr/bin/python3
""" Task 7 """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv[1:]
file = "add_item.json"

try:
    with open(file) as f:
        data_obj = load_from_json_file(file)
except FileNotFoundError:
    data_obj = []

data_obj.extend(args)
save_to_json_file(data_obj, file)
