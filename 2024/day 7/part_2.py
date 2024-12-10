#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=7, year=2024,session=session_id)


data=data.replace(":", "")
data=data.split("\n")
data=[list(d.split(" ")) for d in data]
data = [[int(d) for d in line] for line in data]
print(data)


def verify_line(line):
    result = line[0]
    element_list = line[2:]
    return iterative_solution(element_list, result, line[1])


def iterative_solution(line, result, current_value):
    if current_value > result:
        return False
    if len(line) == 0:
        return current_value == result


    return iterative_solution(line[1:], result, current_value+line[0]) or \
        iterative_solution(line[1:], result, current_value*line[0]) or \
        iterative_solution(line[1:], result, int(str(current_value)+str(line[0])))


answer =  0
for line in data:
    if verify_line(line):
        answer += line[0]
        with open("my_result.txt", "a") as f:
            f.write(f"{line[0]}: {line[1:]}\n")


print(answer)
submit(answer, part="b", day=7, year=2024, session=session_id)