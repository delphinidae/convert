#!/usr/bin/python3
import argparse
import os
import math
import sys
import collections
import importlib


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


#Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input', help='input file path')
parser.add_argument('-o', dest='output', help='output file path')
parser.add_argument('-m', default='json_plugin.py', dest='module_name', help='Way to the module file (including filename extension)')
parser.add_argument('-c', default='JsonLine', dest='class_name', help='Name of a class with process_line function')
args = parser.parse_args()

if args.input is None:
    raise Exception("Input file name is not specified")
if args.output is None:
    raise Exception("Outpput file name is not specified")

#Loading modules
module_name = parse_plugin_path(args.module_name)
#m = __import__(module_name)
try:
    m = importlib.import_module(module_name)
except NameError:
    raise Exception("Maybe {0}.py is not correct python file?".format(module_name))
print("Using {0} for processing".format(module_name))
class_name = getattr(m, args.class_name)
line = class_name()

file_size = os.path.getsize(args.input)
if file_size <= 1:
    raise Exception("File is too small")

#Opening files
with open(args.input, 'r') as f_in:
    with open(args.output, 'w') as f_out:

        columns = f_in.readline().strip("\r\n")
        if len(columns) == 0:
            raise Exception("No columns found")

        processed_size = len(columns)  # not exectly, but who cares
        line_counter = 1

        line_dict = process_columns(columns)
        #Preparing statusbar
        ten_percent_size = file_size / 10
        if file_size > 50000:
            mod_lines = math.floor(file_size / 5000)
        else:
            mod_lines = 10000

        #Processing lines
        for input_line in f_in:
            line_counter += 1
            processed_size += len(input_line)

            if line_counter % mod_lines == 0 and ten_percent_size > 5000:
                print("Approximately {0}% reached".format(math.floor((processed_size / file_size) * 100)))

            cutted_line = cut_line(input_line, line_counter)

            input_list = split_line(cutted_line, len(line_dict), line_counter)

            for cc, ll in zip(line_dict.keys(), input_list):
                line_dict[cc] = ll

            result_string = line.process_line(line_dict, line_counter)

            f_out.write(result_string)
            f_out.write("\n")
