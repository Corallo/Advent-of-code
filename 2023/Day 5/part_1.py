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

min_val = 9999999999999999
for seed in seeds:
    print("Seed n. ", seed)
    val = seed
    for stage in conversions_stages:
        for conversion in stage:
            if val >= conversion[1] and val < conversion[1]+conversion[2]:
                val = val - conversion[1] + conversion[0]
                break
        print(val)
    if val < min_val:
        min_val = val
print("result:", min_val)

assert min_val != 481772950
puzzle.answer_a = min_val