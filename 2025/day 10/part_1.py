#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import re
from ortools.sat.python import cp_model
session_id = open("Session", "r").read()
data = get_data(day=10, year=2025, session=session_id)
#with open("./2025/day 10/data.txt", "r") as f:
#    data = f.read()
data = data.splitlines()
re = re.compile(r"^(\S+)\s+(.*)\s+(\S+)$")
parsed_data = []
for line in data:
    match = re.match(line)
    if match:
        lights = match.group(1)[1:-1]
        buttons = match.group(2).strip().split()
        buttons = [tuple(map(int, part[1:-1].split(","))) for part in buttons]
        fuse = match.group(3)
        parsed_data.append((lights, buttons, fuse))
data = parsed_data
answer=0
for line in data:
    lights, buttons, fuse = line
    print("Lights:", lights)
    print("Buttons:", buttons)
    print("Fuse:", fuse)
    print()
    model = cp_model.CpModel()

    buttons_var = [model.NewBoolVar(f"x_{j}") for j in range(len(buttons))]
    for i, light in enumerate(lights):
        # Sum of buttons that affect light i
        controlled = [buttons_var[j] for j in range(len(buttons)) if i in buttons[j]]
        S_i = model.NewIntVar(0, len(controlled), f"s_{i}")
        model.Add(S_i == sum(controlled))
        target = 1 if light == "#" else 0
        model.AddModuloEquality(target, S_i, 2)

    model.Minimize(sum(buttons_var))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    answer += sum(solver.Value(buttons_var[j]) for j in range(len(buttons)))

print("Answer:", answer)
submit(answer, part="a", day=10, year=2025, session=session_id)