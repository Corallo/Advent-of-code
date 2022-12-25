import numpy as numpy

with open('./Day 17/delta.txt') as f:
    lines = f.readlines()
gL = [int(line.strip()) for line in lines]

start_rep_index = 5000
data = gL[start_rep_index:]
pre_pattern_size = sum(gL[:start_rep_index])

print(len(data))

def find_pattern(data,size):
    #print("Finding pattern", data[:size])
    for i in range(size,len(data)-1):
        if data[i:i+size] == data[:size]:
            #print(data[i:i+size])
            return i

def verify_pattern(data, size,total_size):
    print("Verifying pattern")
    for i in range((total_size)//size):
        if data[i*size:(i+1)*size] != data[:size]:
            print("Error")
            return False
    return True

rep_size = find_pattern(data,100000)
print("After ",start_rep_index,"Size repeat every ", rep_size)
pattern_size = sum(data[:rep_size])
verify_pattern(data, rep_size,1000000000000)
#Found 1745

target_size = 1000000000000 
target_size -= start_rep_index
repetitions = target_size // rep_size
extra_size = target_size % rep_size

print(repetitions, extra_size, pattern_size)
print("Final size: ", pattern_size*repetitions + pre_pattern_size + sum(data[:extra_size]) )
#1569054441256 too high
#1569054441248 too high
#1569054439676 too low
#1569054441243
