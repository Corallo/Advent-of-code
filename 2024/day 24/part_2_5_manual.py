#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
import numpy as np
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt
from z3 import Solver, Bool, Xor, Int, sat, If, Sum, Implies, Not, Or, And, set_option, unsat
DAY=24
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

#set_option('verbose', 10)

with open(f'day {DAY}/input.txt', 'r') as file:
    data = file.read()

inputs, rules = data.split("\n\n")
inputs = [[i.split(": ")[0], int(i.split(": ")[1])] for i in inputs.split("\n")]
#print(inputs)

pattern = r'(\w+)\s+(XOR|OR|AND)\s+(\w+)\s+->\s+(\w+)'
rules = re.findall(pattern, rules)
#print(rules)
bit_to_process= 90
x = 0
y = 0
for i,inp in enumerate(inputs):
    if inp[0].startswith("x") and int(inp[0][1:]) < bit_to_process:
        x += 2**int(inp[0][1:]) * inp[1]
print(x)
for i,inp in enumerate(inputs):
    if inp[0].startswith("y") and int(inp[0][1:]) < bit_to_process:
        y += 2**int(inp[0][1:]) * inp[1]
print(y)

z = x + y
# print z in binary
print(z)
z_str = bin(z)[2:]
print(z_str)


solver = Solver()
variables = {}
for i in inputs:
    if(int(i[0][1:]) < bit_to_process):
        variables[i[0]] = Bool(i[0])
        solver.add(variables[i[0]] == bool(i[1]))

possible_outputs= []

for r in rules:
    variables[r[0]] = Bool(r[0])
    variables[r[2]] = Bool(r[2])
    variables[r[3]] = Bool(r[3])




for i,rule in enumerate(rules):
    if rule[1] == "XOR":
        rule_logic =  variables[rule[3]] == Xor(variables[rule[0]], variables[rule[2]])
    elif rule[1] == "OR":
        rule_logic = rule_logic = variables[rule[3]] == Or(variables[rule[0]], variables[rule[2]])
    elif rule[1] == "AND":
        rule_logic =  rule_logic = variables[rule[3]] == And(variables[rule[0]], variables[rule[2]])
    solver.add(rule_logic)



z_str = z_str[::-1]
for z_bit in range(len(z_str)):
    solver.add(variables[f"z{z_bit:02d}"] == (z_str[z_bit] == "1"))
#print(solver)


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

# sort solution_dict by key
solution_dict = dict(sorted(solution_dict.items(), key=lambda x: x[0]))
print(solution_dict)
answer = 0
for i, a in enumerate(solution_dict):
    if i >= len(z_str):
        continue
    value = model.eval(solution_dict[a])
    answer += 2**i * int(value.as_long())


print(answer, z_str[::-1])
print(x, bin(x)[2:])
print(y, bin(y)[2:])

# First issue at bit 7, it looks like all the z should have as input XOR gate
# Figure 1 shows that cds should be connected to z07, instead, cds XOR rkv -> rts
# TODO: I will swap rts with z07 - That fixed the issue
# Next issue at bit 12, Figure 2 shows that nft and ksn are wrongly connected
# Looking at the graph and the input it looks like ksn XOR nft -> jpj is connected with a xor instead of an AND gate
# TODO: Swapping ksn AND nft -> z12 with ksn XOR nft -> jpj
# Next issue at bit 34, even if this check shows the problem at bit 34, there is probably an issue before by looking ath the graph
# The issue seems to be x26 AND y26 -> z26 they should not be directly connected to z26, there are only 2 nodes wrongly connected (kgj, www), i guess kgj is the problem
# TODO: swap x26 AND y26 -> z26 with bvp XOR gdb -> kgj
# Now the graph looks good, there is still an issue with bit 34.
# the issue seems to be with chv and vvw
# TODO: swapping chv with vvw

# swapped gate are vvw, chv, z26, kgj, jpj, z12, z07, rts
# which sorted are
# chv,jpj,kgj,rts,vvw,z07,z12,z26

#submit(answer, part="b", day=DAY, year=2024, session=session_id)