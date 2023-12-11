from aocd.models import Puzzle
import re
import numpy as np
YEAR = 2023
DAY = 9
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)

# split by \n and convert to int
data = data.split("\n")
print(data)
data = [[int(x) for x in line.split(" ") ] for line  in data]
print(data)


def reduce_list(_list):
    #return the difference between the list[:] and list[1:]
    return [_list[i+1] - _list[i] for i in range(len(_list)-1)]

result = 0
for line in data:
    oasis = [line]
    #itarete until oasasis[-1] is a list of only zeros
    while not all(v == 0 for v in oasis[-1]):
        oasis.append(reduce_list(oasis[-1]))
    print(oasis)

    # sum the last element of each list in oasis
    count = 0
    for line in oasis:
        count += line[-1]
    print(count)
    result += count

print(result)
puzzle.answer_a = result