#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
from z3 import *

DAY=13
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""


problems=data.split("\n\n")

def parse_problem(problems):
    numbers = re.findall(r"[-+]?\d+", problems)
    numbers = [int(n) for n in numbers]
    return numbers

def solve_problem(problem_data):
    push_a = Int('a')
    push_b = Int('b')
    constraints = []
    constraints.append(push_a * problem_data[0] + push_b * problem_data[2] == problem_data[4])
    constraints.append(push_a * problem_data[1] + push_b * problem_data[3] == problem_data[5])
    s = Solver()
    s.add(constraints)
    if s.check() == sat:
        model = s.model()
        return model[push_a].as_long()*3 + model[push_b].as_long()
    return 0


pushes = sum(solve_problem(parse_problem(problem)) for problem in problems)

print(pushes)
submit(pushes, part="a", day=DAY, year=2024, session=session_id)