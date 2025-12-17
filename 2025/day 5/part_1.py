#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=5, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
ranges, ids = data.split("\n\n")
print("Ranges:", ranges)
print("IDs:", ids)
ids = ids.split("\n")
ranges = ranges.split("\n")
range_list = [r.split("-") for r in ranges]
print("Range List:", range_list)


def is_in_range(num, range_list):
    for r in range_list:
        low, high = int(r[0]), int(r[1])
        if low <= num <= high:
            return True
    return False
answer = sum([is_in_range(int(i), range_list) for i in ids])
print(answer)
submit(answer, part="a", day=5, year=2025, session=session_id)