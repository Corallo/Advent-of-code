#Read input file
input_file = open("input.txt", "r")
data = input_file.read()

#Split data into list of strings
data = data.split("\n")
max = []
tmp = 0
for element in data:
    if element == "":
        max.append(tmp)
        tmp = 0
    else:
        tmp += int(element)

max.sort()
# sum the last 3 elements
print(sum(max[-3:]))