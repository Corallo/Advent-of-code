from aocd.models import Puzzle

YEAR = 2023
DAY = 5
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)

data = data.split("\n\n")
print(data)

data = [x.split("\n") for x in data]
print(data)
seeds = [int(x) for x in  data[0][0].split(": ")[1].split(" ")]
print(seeds)
data = [y[1:] for y in data[1:]]
print(data)
conversions_stages = [[list(map(int, nums.split())) for nums in sub_list] for sub_list in data]
print(conversions_stages)

min_val = min(list(map(lambda x: x[0], conversions_stages[-1])))
print(min_val)

puzzle.answer_b = min_val