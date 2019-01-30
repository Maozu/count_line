import json


import os

number = {}


class Suffix(object):
    pass


def read(path):
    global number
    suffix_name = os.path.splitext(path)[1]
    if suffix_name in number:
        number[suffix_name].file_number += 1
        try:
            with open(path, 'r') as f:
                count = len(f.readlines())
                number[suffix_name].line_number += count
        except Exception as error:
                print('Can not open file ', path, '\nReason:', error)
    else:
        s = Suffix()
        s.file_number = 1
        try:
            with open(path, 'r') as f:
                count = len(f.readlines())
            s.line_number = count
            number[suffix_name] = s
        except Exception as error:
            print('Can not open file ', path, '\nReason:', error)


with open('config.json') as config_f:
    DATA = json.load(config_f)
for walk_through in os.walk(DATA["PATH"]):
    for everyone in walk_through[2]:
        file_sux = os.path.splitext(everyone)
        if (file_sux[1] in DATA["COUNT_FILE"]) & (file_sux not in DATA["IGNORE_FILE"]):
            read(os.path.join(walk_through[0], everyone))
for keys, values in number.items():
    print(str(keys).rjust(6) + ': have' + str(values.file_number).rjust(5) + ' files, and' + str(values.line_number).rjust(7) + ' lines')

