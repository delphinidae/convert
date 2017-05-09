import sys
import collections


def parse_plugin_path(module_file):
    if module_file.endswith(".py"):
        module_file = module_file[:-len(".py")]
    else:
        raise Exception("Processing module is not a python file!")
    index = module_file.rfind("/")
    if index == -1:  # not found
        return module_file
    else:
        sys.path.append(module_file[:index])
        return module_file[index + 1:]


def cut_line(input_line, line_counter):
    cutted_line = input_line.strip("\r\n")
    if len(cutted_line) == 0:
        raise Exception("Empty line {0}".format(line_counter))
    return cutted_line


def split_line(cutted_line, dict_len, line_counter):
    input_list = cutted_line.split("\t")
    if len(input_list) != dict_len:
        raise Exception("The wrong column number in line {0}. There shoud be {1} columns, {2} found".format(line_counter, dict_len, len(input_list)))
    return input_list


def process_columns(columns):
    column_list = columns.rstrip().split("\t")
    if len(column_list) > len(set(column_list)):
        raise Exception("Columns should be unique!")
    line_dict = collections.OrderedDict()
    for l in column_list:
        line_dict[l] = ""
    return line_dict
