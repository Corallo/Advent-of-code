#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import numpy as np

session_id = open("Session", "r").read()
data = get_data(day=6, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
print(data)

data = [line for line in data.splitlines()]
# last row contains operations, space between elements determine column width
column_widths = []  
current_width = 0
for i in range(len(data[-1])):
    if data[-1][i] != " ":
        column_widths.append(current_width)
        current_width = 1
    else:
        current_width += 1
column_widths.append(current_width)
column_widths = column_widths[1:]
print("Column Widths:", column_widths)
for line in data:
    assert len(line) == sum(column_widths), "Line length does not match column widths"

arr = np.array([list(line) for line in data])
print(arr)

def mul_op(a,b):
    return a*b
def add_op(a,b):
    return a+b

op_dict = {"*": mul_op,
            "+": add_op}

def parse_column(arr, column_widths, col_idx):
    start_idx = sum(column_widths[:col_idx])
    end_idx = start_idx + column_widths[col_idx]
    op = op_dict[arr[-1, start_idx]]
    return arr[:-1,start_idx:end_idx], op

answer = 0
for i in range(len(column_widths)):
    col_data, operation = parse_column(arr, column_widths, i)
    print(f"Column {i} data:\n{col_data}\nOperation: {operation}")
    values = []
    print(col_data.shape)
    result = 0
    for j in range(col_data.shape[1]):
        if np.all(col_data[:, j] == " "):
            continue
        value_str = "".join(col_data[:, j]).strip()
        values.append(int(value_str))
        if result == 0:
            result = int(value_str)
        else:
            result = operation(result, int(value_str))
    print(values, result)
    answer += result


submit(answer, part="b", day=6, year=2025, session=session_id)