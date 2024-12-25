#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle

import numpy as np

DAY=25
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n\n")
data = [d.split("\n") for d in data]
print(data)
print(len(data))

keys = []
locks = []

for d in data:
    if d[0][0] == ".":
        keys.append(d)
    else:
        locks.append(d)

print(keys)

def key_to_code(key):
    key_code = []
    np_key = np.array([list(s) for s in key])
    for row in range(len(key[0])):
        key_code.append(np.sum(np_key[:,row]=="#")-1)
    return np.array(key_code)

keys = np.array([key_to_code(key) for key in keys])
locks = np.array([key_to_code(lock) for lock in locks])

matches = (keys[:, None, :] + locks) < 6
valid_matches = np.all(matches, axis=2)
counter = np.sum(valid_matches)

print(counter)
submit(counter, part="a", day=DAY, year=2024, session=session_id)