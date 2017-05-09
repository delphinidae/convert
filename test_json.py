# -*- coding: utf8 -*-
import json_plugin
import pytest
import collections


line = json_plugin.JsonLine()
line_dict = collections.OrderedDict()


def test_quots1():
    line_dict["name"] = "Pe't'ya"
    assert line.process_line(line_dict, 0) == '{"name": "Pe\'t\'ya"}'


def test_quots2():
    line_dict.clear()
    line_dict['name'] = 'Pe"t"ya'
    assert line.process_line(line_dict, 0) == '{"name": "Pe\\\"t\\\"ya"}'


def test_tab_columns1():
    line_dict.clear()
    line_dict["name"] = "Petya"
    line_dict["some_string"] = "flrgnn"
    line_dict["num"] = "4"
    assert line.process_line(line_dict, 0) == '{"name": "Petya", "some_string": "flrgnn", "num": "4"}'


def test_tab_columns2():
    line_dict.clear()
    line_dict["name"] = "Petya"
    line_dict["some_string"] = ""
    line_dict["num"] = "4"
    assert line.process_line(line_dict, 0) == '{"name": "Petya", "num": "4"}'


def test_numbers1():
    line_dict.clear()
    line_dict["name"] = "Petya"
    line_dict["num:number"] = "4"
    assert line.process_line(line_dict, 0) == '{"name": "Petya", "num": 4}'


def test_numbers2():
    line_dict.clear()
    line_dict["name"] = "Petya"
    line_dict["num:number"] = "9o"
    with pytest.raises(Exception) as excinfo:
        line.process_line(line_dict, 0)
    assert excinfo.value.message == 'num in line 0 supposed to be a number, but it isn\'t'


def test_cyrillic():
    line_dict.clear()
    line_dict["name"] = u"Петя"
    assert line.process_line(line_dict, 0) == u'{"name": "Петя"}'
