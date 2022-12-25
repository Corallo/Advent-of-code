import numpy as np
from scipy import ndimage

#To complete this challenge I read the solution thread to find out about binary_fill_holes and binary_structure.

#read file
with open("Day 18/input.txt") as f:
    lines = f.readlines()

lines = [line.strip().split(",") for line in lines]
lines = [[int(line[0]), int(line[1]), int(line[2])] for line in lines]

flying_lava = np.zeros((50, 50, 50), dtype=np.int64)

for x, y, z, in lines:
    # Add 1 to each coordinate to make the array 1-based
    flying_lava[x+1, y+1, z+1] = 1
    
flying_lava_filled = ndimage.binary_fill_holes(flying_lava).astype(int)
print(flying_lava_filled.shape)


lava_idx = np.where(flying_lava_filled == 1)
exposed_surfaces = 0
kernel = ndimage.generate_binary_structure(3, 1)
for x, y, z in zip(*lava_idx):
    # Count how many 0s are around each 1
    subset = flying_lava_filled[x-1:x+2, y-1:y+2, z-1:z+2]
    inverse = np.logical_not(subset)
    exposed_surfaces += np.sum(kernel * inverse)
print(exposed_surfaces)

