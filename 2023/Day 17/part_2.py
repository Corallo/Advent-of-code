from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import heapq

YEAR = 2023
DAY = 17
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

#data = "111111111111\n999999999991\n999999999991\n999999999991\n999999999991"
data=data.splitlines()


#Convert data in numpy array of ints
data = np.array([[int(c) for c in row] for row in data])
print(data)


def min_sum_path(matrix):

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0),  (0, -1), (-1, 0)]

    # Priority queue to store (sum, timer, (pos_r, pos_c) (last_dir_r, last_dir_c)) tuples
    pq = []
    pq.append((0, 1, (0, 0), (0, 1)))
    pq.append((0, 1, (0, 0), (1, 0)))
    visited = set()
    predecessors = {}
    while pq:
        current_sum, current_t, pos, last_dir = heapq.heappop(pq)
        row, col = pos
        # Check if we reached the bottom-right corner

        if row == rows - 1 and col == cols - 1 and current_t >= 4:
            path = [(rows - 1, cols - 1)]
            b_current_sum = current_sum
            while (row, col) != (0, 0):
                b_current_sum, current_t, pos, last_dir =  predecessors[(b_current_sum, current_t, pos, last_dir)]
                row, col = pos
                path.append((row, col))
            return current_sum, path[::-1]

        if (current_t, pos, last_dir) in visited:
            continue
        visited.add((current_t, pos, last_dir))

        for dir in directions:
            # No U turns
            if dir == (-last_dir[0], -last_dir[1]):
                continue
            t = current_t + 1
            if dir == last_dir:
                if t > 10:
                    continue
            else:
                if t <=4:
                    continue
                t = 1


            new_row, new_col = row + dir[0], col + dir[1]

            # Check if the new position is within bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Calculate the new sum and add to the priority queue
                new_sum = current_sum + matrix[new_row][new_col]
                heapq.heappush(pq, (new_sum, t, (new_row, new_col), dir))

                predecessors[(new_sum, t, (new_row, new_col), dir)] = (current_sum, current_t, pos, last_dir)

result,path = min_sum_path(data)
print(result)

for el in path:
    data[el[0],el[1]] = "0"

print(data)


assert result > 732
puzzle.answer_b = result