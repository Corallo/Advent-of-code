#read file
with open("Day 21/input3.txt") as f:
    data = f.readlines()

data = [line.strip().split(": ") for line in data]
data = {line[0]: line[1].split(", ")[0] for line in data}


def pre_process_input (data):
    #for each element in data, if it is a number then convert it to an int
    for key in data:
        if data[key].isdigit():
            data[key] = int(data[key])
    return data

data = pre_process_input(data)

def simplify_expression(data, key):

    if type(data[key])==int:
        return data[key]
    else:
        partA = data[key].split(" ")[0]
        partB = data[key].split(" ")[2]
        operation = data[key].split(" ")[1]
        if operation == "+":
            return simplify_expression(data, partA) + simplify_expression(data, partB)
        elif operation == "*":
            return simplify_expression(data, partA) * simplify_expression(data, partB)
        elif operation == "-":
            return simplify_expression(data, partA) - simplify_expression(data, partB)
        elif operation == "/":
            return simplify_expression(data, partA) / simplify_expression(data, partB)

print(simplify_expression(data, "root"))
print(simplify_expression(data, "mrnz"), simplify_expression(data, "jwrp"))


    
    

