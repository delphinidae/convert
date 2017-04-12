#!/usr/bin/python3
import collections
import json


class JsonLine(object):

    def process_line(self, input_dict, line_num):

        result = collections.OrderedDict()

        for cc, ll in input_dict.items():
            if len(ll) == 0:  # write nothing as output
                continue
            num_str = ":number"
            num_length = len(num_str)
            if num_str in cc:  # process numbers
                if ll.isdigit():
                    result[cc[:-num_length]] = int(ll)  # int

                else:  # float
                    try:
                        result[cc[:-num_length]] = float(ll)
                    except ValueError:
                        raise Exception("{0} in line {1} supposed to be a number, but it isn't".format(cc[:-num_length], line_num))
            else:
                result[cc] = ll

        output_string = json.dumps(result, ensure_ascii=False, sort_keys=False)
        return output_string
