#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from tqdm import tqdm

session_id = open("Session", "r").read()
data = get_data(day=3, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
data = data.split("\n")
answer = 0

def find_max_power(current_solution: str, depth, digits: str) -> int:
    if depth == 1:
        return int("".join(current_solution + max(digits)))
    aviable_ditigs = digits[:-(depth-1)]
    max_digit=max(aviable_ditigs)
    current_solution += max_digit
    return find_max_power(current_solution, depth-1, digits[digits.index(max_digit)+1:])

for d in tqdm(data):
    max_power = find_max_power("", 12, d)
    print(max_power)
    answer += max_power
        
print("Solution:", answer)
submit(answer, part="b",  day=3, year=2025, session=session_id)