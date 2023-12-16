from aocd.models import Puzzle
import numpy as np
import re
YEAR = 2023
DAY = 15
puzzle = Puzzle(year=YEAR, day=DAY)


pattern = re.compile(r'([a-zA-Z]+)([^a-zA-Z])(\d*)')
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

boxes = [[] for i in range(256)]

for element in data:

    match = pattern.match(element)
    label = match.group(1)
    symbol = match.group(2) if match.group(2) else None
    number = int(match.group(3)) if match.group(3) else None
    position = hash_function(label)

    #verify if box[position] contains already the label
    if symbol == "=":
        if any([label == box[0] for box in boxes[position]]):
            for box in boxes[position]:
                if box[0] == label:
                    box[1] = number
                    break
        else:
            boxes[position].append([label, number])
    elif symbol == "-":
        #remove label from box[position]
        for box in boxes[position]:
            if box[0] == label:
                boxes[position].remove(box)
                break

result = 0
for i, box in enumerate(boxes):
    for j,element in enumerate(box):
        result += (i+1)*(j+1)*element[1]
print(result)


puzzle.answer_b = result