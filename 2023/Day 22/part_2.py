from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm

YEAR = 2023
DAY = 22
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

data = data.splitlines()


data = [line.split("~") for line in data]
data = [[num.split(",") for num in line] for line in data]
data = [[[int(num) for num in coord] for coord in line] for line in data]

max_x = max([max([coord[0] for coord in line]) for line in data])
max_y = max([max([coord[1] for coord in line]) for line in data])
max_z = max([max([coord[2] for coord in line]) for line in data])
#print(data)
print(max_x, max_y, max_z)

#Sort data by z
data = sorted(data, key=lambda x: x[0][2])



space = np.zeros((max_x+1, max_y+1, max_z+1), dtype=int)
space[:,:,0] = 1 #add floor
number_of_blocks = 0


#Initial fall down
for block_id, block in enumerate(data):
    number_of_blocks += 1
    block_start = block[0]
    block_end = block[1]
    x_start, y_start, z_start = block_start
    x_end, y_end, z_end = block_end
    # fall down until it touches another block
    while True:
        if space[x_start:x_end+1, y_start:y_end+1, z_start-1:z_end].sum() > 0:
            break
        z_start -= 1
        z_end -= 1
    space[x_start:x_end+1, y_start:y_end+1, z_start:z_end+1] = block_id+2


# Visualize space in z,y plane
"""
for z in range(space.shape[2]):
    print("z =", z)
    for y in range(space.shape[1]):
        print("".join(["#" if space[x,y,z] != 0 else "." for x in range(space.shape[0])]))
    print()

# Visualize space in z,x plane
for z in range(space.shape[2]):
    print("z =", z)
    for x in range(space.shape[0]):
        print("".join(["#" if space[x,y,z] != 0 else "." for y in range(space.shape[1])]))
    print()
"""

"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.voxels(space[:,:,:5], edgecolor='k')

plt.show()
"""


# For each block, count how many different blocks are one floor under it
essential_blocks = set()
answer = 0
for block_id in range(2, len(data)+2):
    block = np.where(space == block_id)
    block = np.array(block).T
    # Count how many different blocks are one floor under it
    x_min, y_min, z_min = block.min(axis=0)
    x_max, y_max, z_max = block.max(axis=0)

    # count how many different block id are in space[x_min:x_max, y_min:y_max:z_min-1]
    unique = np.unique(space[x_min:x_max+1, y_min:y_max+1, z_min-1])
    unique = np.delete(unique, np.where(unique == 0))
    #print(unique)
    if len(unique) == 1 and unique[0] != 1:
        if unique[0] not in essential_blocks:
            print("block %d is essential because sustain %d"%(unique[0], block_id))
            essential_blocks.add(unique[0])
        #print("Block n.%d at floor %d has an essential block under it" % (block_id, z_min))

    #print("Block n.%d at floor %d has %d different blocks under it" % (block_id, z_min, len(unique)))


def fall_blocks(fall_space):
    moving = True
    while moving:
        moving = False
        for falling_block_id in range(2, len(data)+2):
            falling_block = np.where(fall_space == falling_block_id)
            falling_block = np.array(falling_block).T

            # if block is an empty list, continue
            if falling_block.shape == (0,3):
                continue

            #print(falling_block)
            # Count how many different blocks are one floor under it
            x_min, y_min, z_min = falling_block.min(axis=0)
            x_max, y_max, z_max = falling_block.max(axis=0)

            #Remove block from current position
            fall_space[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1] = 0
            #make it fall down until it touches another block
            while True:
                if fall_space[x_min:x_max+1, y_min:y_max+1, z_min-1:z_max].sum() > 0:
                    break
                z_min -= 1
                z_max -= 1
                moving = True
            fall_space[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1] = falling_block_id


def conunt_diff_blocks(space, origina_space):
    counter = 0
    for block_id in range(2, len(data)+2):
        block = np.where(space == block_id)
        block = np.array(block).T
        if block.shape == (0,3):
            continue
        # Count how many different blocks are one floor under it
        x_min, y_min, z_min = block.min(axis=0)
        x_max, y_max, z_max = block.max(axis=0)

        if not np.array_equal(space[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1], origina_space[x_min:x_max+1, y_min:y_max+1, z_min:z_max+1]):
            counter += 1
    return counter



#Try to remove one by one the essential blocks, simulate falling, and count how many blocks moved
origina_space = np.copy(space)

falled_blocks = 0
for block_id in tqdm(essential_blocks):
    space = np.copy(origina_space)
    #print("Removing block %d"%block_id)
    space = np.where(space == block_id, 0, space)
    fall_blocks(space)
    new_falled = conunt_diff_blocks(space, origina_space)
    #print("Falled %d blocks"%new_falled)
    falled_blocks += new_falled

print("Falled %d blocks"%falled_blocks)


puzzle.answer_b = falled_blocks