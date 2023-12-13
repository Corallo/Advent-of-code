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


def find_horizontal_simmetry(pattern):
    _simmetries = []
    for reflex_index in range(1,len(pattern)):
        lower_half = pattern[reflex_index:]
        upper_half = pattern[:reflex_index][::-1]
        min_length = min(len(upper_half), len(lower_half))
        upper_half = upper_half[:min_length]
        lower_half = lower_half[:min_length]
        if np.all(upper_half == lower_half):
            _simmetries.append(reflex_index)
    return _simmetries

def find_vertical_simmetry(pattern):
    return find_horizontal_simmetry(pattern.T)

def find_simmetry(pattern):
    _simmetries = []
    vs = find_vertical_simmetry(pattern)
    for sim in vs:
        _simmetries.append((1,sim))
    hs = find_horizontal_simmetry(pattern)
    for sim in hs:
        _simmetries.append((100,sim))
    return _simmetries

def generate_new_pattern(pattern):
    for i in range(pattern.shape[0]):
        for j in range(pattern.shape[1]):
            if pattern[i][j] == 0:
                _new_pattern = pattern.copy()
                _new_pattern[i][j] = 1
                yield _new_pattern
            else:
                _new_pattern = pattern.copy()
                _new_pattern[i][j] = 0
                yield _new_pattern

result = 0
for _pattern in patterns:

    original_simmetry = find_simmetry(_pattern)[0]
    for new_pattern in generate_new_pattern(_pattern):
        new_simmetry = find_simmetry(new_pattern)
        if original_simmetry in new_simmetry:
            new_simmetry.remove(original_simmetry)
        #new symmetry is not empty list
        if new_simmetry:
            new_simmetry = new_simmetry[0]
            result += new_simmetry[0] * new_simmetry[1]
            break


print(result)
puzzle.answer_b = result