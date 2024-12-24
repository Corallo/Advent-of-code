#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
from tqdm import tqdm
from functools import lru_cache

DAY=19
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

towels, patterns = data.split("\n\n")

print(towels)
towels = towels.split(", ")
patterns = patterns.split("\n")


@lru_cache
def compose_pattern(target_pattern):
    if target_pattern == "":
        return 1
    out = 0
    for t in towels:
        if t == target_pattern[:len(t)]:
            out += compose_pattern(target_pattern[len(t):])
    return out


result = 0
for p in tqdm(patterns):
    out = compose_pattern(p)
    result += out
    print (p, out)

print(result)

submit(result, part="b", day=DAY, year=2024, session=session_id)