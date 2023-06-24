#!/usr/bin/python3
""" Task 7 """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv[1:]
filename = "add_item.json"

try:
    existing_data = load_from_json_file(filename)
    data = existing_data + args
except FileNotFoundError:
    data = args

save_to_json_file(data, filename)
