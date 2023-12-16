from aocd.models import Puzzle
import numpy as np
YEAR = 2023
DAY = 15
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

data=data.split(",")
print(data)

def hash_function(line):
    value = 0
    for ch in line:
        value += ord(ch)
        value *= 17
        value %= 256
    return value

result = 0
for line in data:
    val = hash_function(line)
    result += val
    print(hash_function(line))


print(result)
puzzle.answer_a = result