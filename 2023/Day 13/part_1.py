from aocd.models import Puzzle
import numpy as np
YEAR = 2023
DAY = 13
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
#Convert data into 0 and 1
data=data.replace(".", "0")
data=data.replace("#", "1")
data = data.split("\n\n")


patterns = [pattern.split("\n") for pattern in data]
#convert patterns into numpy arrays of ints
patterns = [np.array([[int(digit) for digit in str(number)] for number in arr]) for arr in patterns]

print(patterns[1])

def find_horizontal_simmetry(pattern):
    for reflex_index in range(1,len(pattern)):
        lower_half = pattern[reflex_index:]
        upper_half = pattern[:reflex_index][::-1]
        min_length = min(len(upper_half), len(lower_half))
        upper_half = upper_half[:min_length]
        lower_half = lower_half[:min_length]
        if np.all(upper_half == lower_half):
            return reflex_index
    return 0

def find_vertical_simmetry(pattern):
    return find_horizontal_simmetry(pattern.T)


result = 0
for pattern in patterns:
    result += find_horizontal_simmetry(pattern)*100 + find_vertical_simmetry(pattern)

print(result)

puzzle.answer_a = result