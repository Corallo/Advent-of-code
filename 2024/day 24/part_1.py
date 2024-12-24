#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
from z3 import Solver, Bool, Xor, sat, If
DAY=24
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

inputs, rules = data.split("\n\n")
inputs = [[i.split(": ")[0], int(i.split(": ")[1])] for i in inputs.split("\n")]
print(inputs)

pattern = r'(\w+)\s+(XOR|OR|AND)\s+(\w+)\s+->\s+(\w+)'
rules = re.findall(pattern, rules)
print(rules)

solver = Solver()
variables = {}
for i in inputs:
    variables[i[0]] = Bool(i[0])
    solver.add(variables[i[0]] == bool(i[1]))

for r in rules:
    variables[r[0]] = Bool(r[0])
    variables[r[2]] = Bool(r[2])
    variables[r[3]] = Bool(r[3])

for rule in rules:
    if rule[1] == "XOR":
        solver.add(variables[rule[3]] == Xor(variables[rule[0]], variables[rule[2]]))
    elif rule[1] == "OR":
        solver.add(variables[rule[0]] | variables[rule[2]] == variables[rule[3]])
    elif rule[1] == "AND":
        solver.add(variables[rule[0]] & variables[rule[2]] == variables[rule[3]])

if solver.check() == sat:
    model = solver.model()
    print(model)
    solution_dict = {}

    for a in variables:
        if a.startswith("z"):
            solution_dict[a] =  If(model[variables[a]], 1, 0)

    print(solution_dict)

    solution_dict = dict(sorted(solution_dict.items(), key=lambda x: x[0]))
    print(solution_dict)
    answer = 0
    for i, a in enumerate(solution_dict):
        value = model.eval(solution_dict[a])
        answer += 2**i * int(value.as_long())
    print(answer)



submit(answer, part="a", day=DAY, year=2024, session=session_id)