#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from skimage.morphology import flood, flood_fill
from shapely.geometry import Polygon
from skimage.measure import find_contours
import matplotlib.pyplot as plt


DAY=12
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data_4.txt', 'r') as file:
    data = file.read()"""

print(data)
data=data.strip().split("\n")
data = np.array([list(d) for d in data])
data = np.vectorize(ord)(data)
print(data)

def calculate_score(grid):

    zones = np.zeros_like(grid, dtype=int)
    connectivity = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]])
    zone_id = 0
    score = 0
    total_area = 0

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if zones[i, j] == 0:  # If not yet visited
                zone_id += 1
                mask = flood(grid, (i, j), footprint=connectivity)
                zones += mask*zone_id
                area= count_area(mask)
                perimeter = count_corners(mask)
                score +=area*perimeter
                total_area += count_area(mask)

    assert total_area == zones.shape[0]*zones.shape[1]
    return score


def count_area(mask):
    return np.sum(mask)

"""Basically:
1. Pad the mask otherwise the poligon is wrong somehow
2. Find the contours of the shape
3. Make a poligon out of it (list of corners)
4. Iterate over the list and if the points are not aligned
(i.e. the difference between the x or y coordinates is 0.5) then it is a corner
5. Corner-case (ah-ah), there could be more corners inside the shape, so we need to find the inner shapes
6. Flood-fill the inverted mask to find those inner shapes
7. repeat the above to find the corners of the inner shapes"""
def count_corners(mask):

    mask = mask.astype(np.uint8)
    mask= np.pad(mask, pad_width=1, mode='constant', constant_values=0)
    contours = find_contours(mask, level=0.5)
    poli=Polygon(contours[0])
    old_point = list(poli.exterior.coords)[0]
    counter = 0

    for point in list(poli.exterior.coords)[1:]:
        if abs(point[0] - old_point[0]) == 0.5 or abs(point[1] - old_point[1]) == 0.5:
            counter +=1
        old_point = point

    inverted_map = 1 - mask
    filled_map = inverted_map.copy()

    fill_footprint = np.array([[1, 1,1],
                                 [1, 1, 1],
                                 [1, 1, 1]])

    # Flood-fill from the edge, because of the padding, it is enough to start from 0,0
    filled_map = flood_fill(filled_map, (0, 0), 0, connectivity=1, footprint=fill_footprint)

    inner_shapes = filled_map

    if np.sum(inner_shapes) == 0:
        return counter

    """# plot mask, inverted, mask and inner shapes side by side (for debugging)
        fig, ax = plt.subplots(2, 2, figsize=(10, 10))
        ax[0,0].imshow(mask, cmap='gray')
        ax[0,0].set_title('Mask')
        ax[0,1].imshow(inverted_map, cmap='gray')
        ax[0,1].set_title('Inner Shapes')
        ax[1,0].imshow(filled_map, cmap='gray')
        ax[1,0].set_title('Inner Shapes')
        plt.show(block=True)"""

    inner_contours = find_contours(inner_shapes, level=0.5)
    inner_polis = [Polygon(contour) for contour in inner_contours]
    for poli in inner_polis:
        old_point = list(poli.exterior.coords)[0]
        for point in list(poli.exterior.coords)[1:]:
            if abs(point[0] - old_point[0]) == 0.5 or abs(point[1] - old_point[1]) == 0.5:
                counter +=1
            old_point = point

    return counter

answer = calculate_score(data)
print(answer)
submit(answer, part="b", day=DAY, year=2024, session=session_id)