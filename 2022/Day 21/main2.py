import z3

with open("Day 21/input2.txt") as f:
    data = f.readlines()

def pre_process_input (data):
    #for each element in data, if it is a number then convert it to an int
    for key in data:
        if data[key].isdigit():
            data[key] = int(data[key])
    return data

data = [line.strip().split(": ") for line in data]
data = {line[0]: line[1].split(", ")[0] for line in data}
data = pre_process_input(data)

z3_vars = {}

z3_vars["humn"] = z3.Real("humn")
for key in data:
    z3_vars[key] = z3.Real(key)

constraints = []
#for each line in data, add a constraint to the solver
for key in data:

    if key == "humn":
        continue
    if type(data[key])==int:
        constraints.append(z3_vars[key] == data[key])
    else:
        partA = data[key].split(" ")[0]
        partB = data[key].split(" ")[2]
        operation = data[key].split(" ")[1]
        if operation == "+":
            constraints.append(z3_vars[key] == z3_vars[partA] + z3_vars[partB])
        elif operation == "*":
            constraints.append(z3_vars[key] == z3_vars[partA] * z3_vars[partB])
        elif operation == "-":
            constraints.append(z3_vars[key] == z3_vars[partA] - z3_vars[partB])
        elif operation == "/":
            constraints.append(z3_vars[key] == z3_vars[partA] / z3_vars[partB])
        elif key == "root":
            constraints.append(z3_vars[partA] == z3_vars[partB])
        
s = z3.Solver()
s.add(constraints)
print(s.check())
print(s.model()[z3.Real("humn")])
print(s.model()[z3.Real(data["root"].split(" ")[0])], s.model()[z3.Real(data["root"].split(" ")[2])])
