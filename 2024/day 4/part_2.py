#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=4, year=2024,session=session_id)

data = data.split("\n")

s1 = len(data)
s2 = len(data[0])


pattern = np.array([ ["M"," ","S"],
            [" ","A"," "],
            ["M"," ","S"]
        ])


def verify_pattern(sub_matrix, pattern):
    if len(sub_matrix) != 3 or len(sub_matrix[0]) != 3:
        return False
    for _ in range(4):
        if pattern[0][0] == sub_matrix[0][0] and \
        pattern[0][2] == sub_matrix[0][2] and \
        pattern[1][1] == sub_matrix[1][1] and \
        pattern[2][0] == sub_matrix[2][0] and \
        pattern[2][2] == sub_matrix[2][2]:
            return True
        pattern = np.rot90(pattern)
    return False


counter = 0
for r in range(s1):
    for c in range(s2):
        if r + 2 < s1 and c + 2 < s2:
            sub_matrix = np.array([list(data[r][c:c+3]), list(data[r+1][c:c+3]), list(data[r+2][c:c+3])])
            if verify_pattern(sub_matrix, pattern):
                counter += 1

print(counter)
submit(counter, part="b", day=4, year=2024, session=session_id)