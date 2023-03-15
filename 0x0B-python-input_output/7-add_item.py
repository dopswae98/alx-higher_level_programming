import json
import os


def load_from_json_file():
    with open("add_item.json", mode='r', encoding='UTF8') as my_file:
        data = json.load(my_file)
        return data


def save_to_json_file(my_obj):
    json_object = json.dumps(my_obj)
    with open("add_item.json", mode='w', encoding='UTF8') as my_file:
        my_file.write(json_object)


def do_everything():
    data = load_from_json_file()
    save_to_json_file(data + ["4", "6"])


do_everything()












