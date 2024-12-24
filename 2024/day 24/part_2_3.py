#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
import numpy as np
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt
from z3 import Solver, Bool, Xor, sat, If, Sum, Implies, Not, Or, And
DAY=24
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

# This solution never worked finished to run
# The idea is to add a layer after every output, that allow to swap the "original" output with another "original" output
# the inputs, always use the "non-original" version after a potential swap
# the swap are decided by z3 solver, that will try allow only 4 swaps
"""with open(f'2024/day {DAY}/input.txt', 'r') as file:
    data = file.read()"""

inputs, rules = data.split("\n\n")
inputs = [[i.split(": ")[0], int(i.split(": ")[1])] for i in inputs.split("\n")]
print(inputs)

pattern = r'(\w+)\s+(XOR|OR|AND)\s+(\w+)\s+->\s+(\w+)'
rules = re.findall(pattern, rules)
print(rules)

x = 0
y = 0
for i,inp in enumerate(inputs):
    if inp[0].startswith("x"):
        x += 2**int(inp[0][1:]) * inp[1]
print(x)
for i,inp in enumerate(inputs):
    if inp[0].startswith("y"):
        y += 2**int(inp[0][1:]) * inp[1]
print(y)

z = x + y
print(z)
z_str = bin(z)[2:]
print(z_str)


solver = Solver()
variables = {}
for i in inputs:
    variables[i[0]] = Bool(i[0])
    solver.add(variables[i[0]] == bool(i[1]))

possible_outputs= []

# Declare variables
for r in rules:
    variables[r[0]] = Bool(r[0])
    variables[r[2]] = Bool(r[2])
    variables[r[3]] = Bool(r[3])
    possible_outputs.append(r[3])
    variables[r[3]+"_original"] = Bool(r[3]+"_original")
    # the "original" version of the node is the node before any wire swapping

# Add logic constraints
for i,rule in enumerate(rules):
    if rule[1] == "XOR":
        rule_logic =  variables[rule[3]+"_original"] == Xor(variables[rule[0]], variables[rule[2]])
    elif rule[1] == "OR":
        rule_logic = rule_logic = variables[rule[3]+"_original"] == Or(variables[rule[0]], variables[rule[2]])
    elif rule[1] == "AND":
        rule_logic =  rule_logic = variables[rule[3]+"_original"] == And(variables[rule[0]], variables[rule[2]])
    solver.add(rule_logic)

pairs = []
# declare swap flags
for i in range(len(possible_outputs)):
    for j in range(i+1, len(possible_outputs)):
        pairs.append((possible_outputs[i], possible_outputs[j]))
swap_flags = [Bool(f'swap_{i}_{j}') for i, j in pairs]

# force 4 swaps
solver.add(Sum([If(flag, 1, 0) for flag in swap_flags]) == 4)

# if we swap i,j we force node_a == node_b_original and node_b == node_a_original
for i, (a, b) in enumerate(pairs):
    solver.add(Implies(swap_flags[i], And(variables[a] == variables[b+"_original"],
                                         variables[b] == variables[a+"_original"])))

# if we never swapped i, then node_a == node_a_original
# Note, this had a bug BBEFORE, now this code it is fine, I explain the old bug below:
# I WAS just using not(swap_flags[i]) instead of all_candidates_false
# that creates a conflict with previous constraints
# e.g. if swap_5_0 is false but swap_5_1 is true, then the first condition would have given
# node_5 == node_5_original, but the second condition would have given node_5 == node_1_original
# that is a contradiction
# with this new code, we say node_i == node_i_original if ALL swap flags that contain i are false
for var in possible_outputs:
    candidates = [swap_flags[i] for i in range(len(pairs)) if var in pairs[i]]
    all_candidates_false = And([Not(c) for c in candidates])
    solver.add(Implies(all_candidates_false, variables[var] == variables[var+"_original"]))


z_str = z_str[::-1]
for z_bit in range(len(z_str)):
    solver.add(variables[f"z{z_bit:02d}"] == Bool(z_str[z_bit]))
print(solver)


if solver.check()  == sat:
    print("sat")
else:
    print("unsat")
    exit()


model = solver.model()
print(model)

solution_dict = {}

for a in variables:
    if a.startswith("z") and not a.endswith("_original"):
        solution_dict[a] =  If(model[variables[a]], 1, 0)

print(solution_dict)

solution_dict = dict(sorted(solution_dict.items(), key=lambda x: x[0]))
print(solution_dict)
answer = 0
for i, a in enumerate(solution_dict):
    value = model.eval(solution_dict[a])
    answer += 2**i * int(value.as_long())
print(answer)

for i, a in enumerate(swap_flags):
    if model[a] == True:
        print(swap_flags[i])

#submit(answer, part="b", day=DAY, year=2024, session=session_id)