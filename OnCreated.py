# -----------------------------------------------------------
# OnCreated.py
# v.1.0
# Updated: 20220807
# Houdini version: 19.5.303, Python 3.9
# Redshift version: 3.5.05
# -----------------------------------------------------------

"""
Operations applied to all nodes in OnCreated event.
"""

import os
from datetime import datetime
import json
from os.path import exists

# Get the node generating the new node.
# node = hou.pwd()

# Get created node.
hou_node = kwargs["node"]

json_path = 'C:/temp/hou_log/hou_node_usage_log.json'


def log_node_entry(node):
    """
    Generate node data to be logged.
    :param node:
    :return:
    """
    node_name = node.name()
    node_type = node.type()
    node_category = node_type.category()
    node_def = node_type.definition()
    # Check if node has definition. Some OOTB nodes are not
    #   constructed with HDA definitions.
    if bool(node_def):
        node_is_current = node_def.isCurrent()
        node_lib_path = node_def.libraryFilePath()
    else:
        node_is_current = 'N/A'
        node_lib_path = 'N/A'

    entry_log_date, entry_log_time = log_date_time()

    node_entry = {'name': node_name,
                  'type': node_type.name(),
                  'category': node_category.name(),
                  'current': node_is_current,
                  'path': node_lib_path,
                  'date': entry_log_date,
                  'time': entry_log_time
                  }
    # node_entry['date'] = datetime_object
    # print('node logged: {}'.format(node_entry))
    return node_entry


def log_node_to_json(new_data, file):
    """
    Add node data entry to json file.
    :param new_data:
    :param file:
    :return:
    """
    with open(file, 'r+') as json_file:
        # First we load existing data into a dict.
        file_data = json.load(json_file)
        # Join new_data with file_data inside emp_details
        file_data["node_details"].append(new_data)
        # Sets file's current position at offset.
        json_file.seek(0)
        # convert back to json.
        json.dump(file_data, json_file, indent=4)


def init_json_file(path):
    """
    Check if file exists or not before executing the following function.
    :param path:
    :return:
    """
    json_start_data = {'node_details': []}
    json_start_string = json.dumps(json_start_data, ensure_ascii=False, indent=4)
    # print(json_start_string)
    with open(path, 'w') as json_file:
        json.dump(json_start_data, json_file, indent=4)


def log_date_time():
    """
    Log current date and time.
    :return:
    """
    now = datetime.now()
    datetime_object = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_object = now.strftime("%m/%d/%Y")
    time_object = now.strftime("%H:%M:%S")
    return date_object, time_object


def log_node(logged_node, path):
    """
    Main function to log node to log file.
    :param logged_node:
    :param path:
    :return:
    """
    node_log_exists = exists(path)
    if not node_log_exists:
        init_json_file(path)
    node_entry = log_node_entry(logged_node)
    log_node_to_json(node_entry, path)


log_node(hou_node, json_path)
