import json
import os
import matplotlib.pyplot as plt
import numpy as np


number = {}
number_save = {}


class Suffix(object):
    pass


def read(path):
    for name in DATA["IGNORE_DIR"]:
        if name in path:
            return
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


lables = []
sizes = []
with open('config.json') as config_f:
    DATA = json.load(config_f)
for walk_through in os.walk(DATA["PATH"]):
    for everyone in walk_through[2]:
        file_sux = os.path.splitext(everyone)
        if (file_sux[1] in DATA["COUNT_FILE"]) & (everyone not in DATA["IGNORE_FILE"]):
            read(os.path.join(walk_through[0], everyone))
for keys, values in number.items():
    print(str(keys).rjust(6) + ': have' + str(values.file_number).rjust(5) + ' files, and' + str(values.line_number).rjust(7) + ' lines')
    lables.append(str(keys)[1:])
    sizes.append(int(values.line_number))

with open('way.json', 'r') as way_f:
    DATA_WAY = json.load(way_f)

for keys, values in number.items():
    DATA_WAY[keys[1:]].append(int(values.line_number) - DATA_WAY.get(keys[1:], 0)[0])
    DATA_WAY[keys[1:]][0] = values.line_number

with open('way.json', 'w') as way_f:
    json.dump(DATA_WAY, way_f, indent=2)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=lables, startangle=90)
plt.show()


# 这一段写的麻烦的和c一样，一定是有问题的，但是怎么搞呢
k = []
v = []
for keys, values in DATA_WAY.items():
    k.append(keys)
    values.pop(0)
    try:
        values[1]
    except:
        pass
    else:
        values.pop(0)
    v.append(values)
i = 0
while i < len(v):
    j = 0
    while j < len(v[0]):
        q = i + 1
        while q < len(v):
            v[i][j] += v[q][j]
            q += 1
        j += 1
    i += 1
ind = np.arange(len(v[0]))
p = []
for i in range(len(v)):
    p.append(plt.bar(ind, v[i]))

plt.ylabel('')
plt.title('')
plt.xticks(ind, range(len(v[0])))
plt.yticks(np.arange(0, 1.5 * v[0][0], 0.1 * v[0][0]))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
for i in range(len(p)):
    p[i] = p[i][0]
plt.legend(p, k)
plt.show()
