#Read input file
input_file = open("input.txt", "r")
data = input_file.read()

#Split data into list of strings
data = data.split("\n")
max = 0
tmp = 0
for element in data:
    if element == "":
        if(max < tmp):
            max = tmp
        tmp = 0
    else:
        tmp += int(element)
print(max)
