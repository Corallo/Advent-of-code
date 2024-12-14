#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
from z3 import *
import numpy as np
import cv2
import re

DAY=14
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""


map_x = 101
map_y = 103
middle_x = map_x // 2
middle_y = map_y // 2
data=data.split("\n")

def parse_robot(line):
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    matches = re.findall(pattern, line)
    return int(matches[0][1]), int(matches[0][0]), int(matches[0][3]), int(matches[0][2])
data=[parse_robot(line) for line in data]

time=0
data_array = np.array(data)
poses = data_array[:, :2]
speeds = data_array[:, 2:]

n_robots = len(data)
debug_map = np.zeros((map_y, map_x), dtype=int)


video_writer = cv2.VideoWriter(
    f"2024/day {DAY}/output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    30,
    (map_x, map_y)
)

frame_count = 0

while frame_count < 10000:
    debug_map.fill(0)
    poses = (poses + speeds)
    poses[:,0] %= map_y
    poses[:,1] %= map_x
    debug_map[tuple(poses.T)] = 1
    frame = (debug_map*255).astype(np.uint8)
    color_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    text = f"Frame: {frame_count}"
    cv2.putText(color_frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255) , 1)
    video_writer.write(color_frame)
    frame_count += 1

video_writer.release()