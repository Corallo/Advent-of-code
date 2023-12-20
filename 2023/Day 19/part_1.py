from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import re

YEAR = 2023
DAY = 19
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

#data = puzzle.examples[0][0]
rules, parts = data.split("\n\n")

#print(rules,parts)


def parse_rules(rules):
    pattern = re.compile(r'([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    rules_dict = {}
    for rule in rules.splitlines():
        name = rule.split("{")[0]
        body = rule.split("{")[1][:-1]
        conditions = body.split(",")
        end_case = [conditions[-1]]
        condisions_parsed = []
        for condition in conditions[:-1]:
            match = pattern.match(condition)
            if match:
                variable = match.group(1)
                op = match.group(2)
                value = int(match.group(3))
                operand = match.group(4)
            else:
                print("Error, missing match")
                print(condition)
                exit()
            condisions_parsed.append((variable, op, value, operand))
        condisions_parsed.append(end_case)
        rules_dict[name] = condisions_parsed

    return rules_dict

def parse_parts(_parts):
    pattern = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    part_list = []
    for part in _parts.splitlines():
        part_compoents = {}
        matches = pattern.match(part)
        part_compoents["x"] = int(matches.group(1))
        part_compoents["m"] = int(matches.group(2))
        part_compoents["a"] = int(matches.group(3))
        part_compoents["s"] = int(matches.group(4))
        part_list.append(part_compoents)
    return part_list


def process_parts(parts,rules):
    queue = []
    score = 0

    for part in parts:
        queue.append((part, "in"))

    while queue:
        part, rule_name = queue.pop(0)
        rule = rules[rule_name]
        for r in rule:
            if len(r)==1:
                if r[0] == "A":
                    score += sum(part.values())
                    break
                if r[0] == "R":
                    break
                queue.append((part, r[0]))
                break
            if r[1] == ">":
                if part[r[0]] > r[2]:
                    if r[3] == "A":
                        score += sum(part.values())
                        break
                    if r[3] == "R":
                        break
                    queue.append((part, r[3]))
                    break
            if r[1] == "<":
                if part[r[0]] < r[2]:
                    if r[3] == "A":
                        score += sum(part.values())
                        break
                    if r[3] == "R":
                        break
                    queue.append((part, r[3]))
                    break
    return score


rules = parse_rules(rules)
parts = parse_parts(parts)
score = process_parts(parts,rules)
print(score)



puzzle.answer_a = score