from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import re

YEAR = 2023
DAY = 19
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
#with open("Day 19/test_file.txt", "r") as f:
#    data = f.read()
rules, parts = data.split("\n\n")

#print(rules,parts)


def parse_rules(rules):
    pattern = re.compile(r'([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    rules_dict = {}
    for rule in rules.splitlines():
        name = rule.split("{")[0]
        body = rule.split("{")[1][:-1]
        conditions = body.split(",")
        end_case = conditions[-1]
        i=0
        for i, condition in enumerate(conditions[:-1]):
            match = pattern.match(condition)
            variable = match.group(1)
            op = match.group(2)
            value = int(match.group(3))
            operand = match.group(4)
            rules_dict[name+str(i)] = [variable, op, value, operand+str(0), name+str(i+1)]
        rules_dict[name+str(i+1)] = [end_case+str(0)]

    return rules_dict

def count_possible_parts(parts):
    total = 1
    for part in parts.values():
        total *= part[1] - part[0]
    return total

#minor_operator
def filter_ranges(range, condition_value, operator, included=False):
    result_range = []
    start, end = range
    if not operator: # True if operator == >
        start = condition_value + (0 if included else 1) -1
    else:
        end   = condition_value - (0 if included else 1)

    if start <= end:
        result_range = [start, end]

    return result_range


def count_combinations(parts, rule_name):
    rule = rules[rule_name]
    combinations = 0
    if parts["x"] == [] or parts["a"] == [] or parts["m"] == [] or parts["s"] == []:
        return 0
    if rule_name=="A0":
        print(parts, count_possible_parts(parts))
        return count_possible_parts(parts)
    if rule_name=="R0":
        return 0
    if len(rule)==1:
        return count_combinations(parts, rule[0])

    tmp_parts_A = parts.copy()
    tmp_parts_A[rule[0]] = filter_ranges(parts[rule[0]], rule[2], rule[1]=="<", included = False)
    combinations += count_combinations(tmp_parts_A, rule[3])
    tmp_parts_B = parts.copy()
    tmp_parts_B[rule[0]] = filter_ranges(parts[rule[0]], rule[2], rule[1]!="<", included = True)
    combinations += count_combinations(tmp_parts_B, rule[4])

    return combinations

rules = parse_rules(rules)
parts = {"x":[0,4000],
         "a":[0,4000],
         "m":[0,4000],
         "s":[0,4000]}
rules["A0"] = ["A"]
rules["R0"] = ["R"]
print(rules)
#print(parts)
score = count_combinations(parts,"in0")
print(score)


assert score < 4000**4
puzzle.answer_b = score