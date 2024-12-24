#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import itertools
DAY=22
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()
"""
data = data.split("\n")

#print(data)

def generate_secret_number(n, iteration):
    prices = []
    for _ in range(iteration):
        prices.append( n % 10 )
        n = ((n * 64) ^ n ) % 16777216
        n = ((n//32) ^ n ) % 16777216
        n = ((n * 2048) ^ n ) % 16777216
    return prices

all_prices = np.array([generate_secret_number(int(d), 2000) for d in data])
print(all_prices.shape)
differentials = np.diff(all_prices, axis=1)
print(differentials.shape)

def find_subarray(large_array, subarray):
    sub_len = len(subarray)
    for i in range(len(large_array) - sub_len + 1):
        if np.array_equal(large_array[i:i + sub_len], subarray):
            return i + sub_len
    return -1

def find_subarray_index_fast(large_array, sub_array):
    large_array = np.array(large_array)
    sub_array = np.array(sub_array)

    n = len(sub_array)
    large_array_windows = np.lib.stride_tricks.sliding_window_view(large_array, n)

    matches = np.all(large_array_windows == sub_array, axis=1)
    indices = np.where(matches)[0]

    return indices[0] + len(sub_array) if indices.size > 0 else -1

def find_subarray_in_matrix(matrix, subarray):
    sub_len = len(subarray)
    indices = np.full(matrix.shape[0], -1)

    for i in range(matrix.shape[1] - sub_len + 1):
        if np.all(matrix[:, i:i + sub_len] == subarray, axis=1).any():
            match = np.where(np.all(matrix[:, i:i + sub_len] == subarray, axis=1))[0]
            indices[match] = i  + sub_len # Update indices for rows where a match is found

    return indices

# Verify all the cumsum (s0+s1, s0+s1+s2, s0+s1+s2+s3) are between -9, 9
def filter_valid_sequences(sequences):
    cumulative_sums = np.cumsum(sequences, axis=1)
    valid_mask = np.all((cumulative_sums >= -9) & (cumulative_sums <= 9), axis=1)
    valid_sequences = sequences[valid_mask]
    return valid_sequences

# generate all possible array of 4 elements from -9 to +9
all_possible_signals = np.array(list(itertools.product(range(-9, 10), repeat=4)))
# sort all_possible signal by the 4th element from high to low
all_possible_signals = all_possible_signals[all_possible_signals.sum(axis=1).argsort()[::-1]]
print(all_possible_signals.shape)

all_possible_signals = filter_valid_sequences(all_possible_signals)
all_possible_signals = all_possible_signals[np.sum(all_possible_signals, axis=1) > 0]

#[ 2 -3 0 3] 2100 (sequence 15000+11000)
print(all_possible_signals.shape)
max_value = 0
N = differentials.shape[0]
for signal in tqdm(all_possible_signals):
    current_value = 0
    for i in range(N):
        idx = find_subarray_index_fast(differentials[i], signal)
        if idx != -1:
            current_value += all_prices[i, idx]
        if current_value + (N-i)*9 < max_value:
            break
    if current_value > max_value:
        max_value = current_value
        print(signal, current_value)
print(max_value)
#submit(answer, part="b", day=DAY, year=2024, session=session_id)

