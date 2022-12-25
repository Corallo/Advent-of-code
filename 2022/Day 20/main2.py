from tqdm import tqdm
#Read input
with open("Day 20/input.txt") as f:
    data = f.read().splitlines()

#parse to int
data = [int(i) for i in data]


# assign an unique id to each element in list
data = [(i, data[i]*811589153) for i in range(len(data))]

output = data.copy()


def rotate_element_right(position, data):
    element = data[position]
    steps = element[1]
    #remove element from list and put it back in position+steps % len(data-1)
    data.pop(position)
    data.insert((position+steps) % (len(data)), element)
    return data

print("Starting output: ")
print([output[j][1] for j in range(len(output))])


for i in tqdm(range(len(output)*10)):
    i=i%len(output)
    #find position element in output[:][0]
    #print("Iteration ", i)
    position = [output[j][0] for j in range(len(output))].index(i)
    rotate_element_right(position, output)
    #Print only element 1 of each tuple
    #print([output[j][1] for j in range(len(output))])

result_positions = [1000,2000,3000]
zero_position = [output[j][1] for j in range(len(output))].index(0)
#print("Position zero", zero_position)
result_positions = [(pos+zero_position)%len(output) for pos in result_positions]
#print("Result positions", result_positions)

print(sum([output[pos][1] for pos in result_positions]))


    
