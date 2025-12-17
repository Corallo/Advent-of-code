#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=5, year=2025, session=session_id)
#with open("./2025/day 5/data.txt", "r") as f:
#    data = f.read()
ranges, ids = data.split("\n\n")
print("Ranges:", ranges)
print("IDs:", ids)
ids = ids.split("\n")
ranges = ranges.split("\n")
range_list = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges]


def find_overlap(range1, range2):
    return max(0, min(range1[1], range2[1]) - max(range1[0], range2[0]) + 1)

def merge_ranges(range1, range2):
    return [min(range1[0], range2[0]), max(range1[1], range2[1])]


sorted_ranges = sorted(range_list, key=lambda x: x[0])
new_ranges = []

for r in sorted_ranges:
    merged = False
    for i in range(len(new_ranges)):
        if find_overlap(r, new_ranges[i]) > 0:
            new_ranges[i] = merge_ranges(r, new_ranges[i])
            merged = True
            break
    if not merged:
        new_ranges.append(r)

print("Merged Ranges:", new_ranges)         
answer = sum(r[1]-r[0]+1 for r in new_ranges)
print(answer)
submit(answer, part="b", day=5, year=2025, session=session_id)