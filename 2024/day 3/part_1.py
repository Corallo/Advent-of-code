#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=3, year=2024,session=session_id)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, data)
print(matches)

result = 0
for match in matches:
    result += int(match[0]) * int(match[1])

print(result)
submit(result, part="a", day=3, year=2024, session=session_id)