from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import re

YEAR = 2023
DAY = 20
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

#data = puzzle.examples[0][0]

print(data)

def parse_schematics(data):
    schematics = {}

    for part in data.splitlines():
        name, targets = part.split(" -> ")
        type = None
        if name[0] == "%":
            name = name[1:]
            type = "flip"
            status = 0
        elif name[0] == "&":
            name = name[1:]
            type = "conj"
            status = {}
        else:
            type = "brod"
            status = None
        targets = targets.split(", ")
        schematics[name] = {"type":type,"outputs": targets,"state": status}

    #Set inital state of conj parts
    for name_conj, part_conj in schematics.items():
        if part_conj["type"] == "conj":
            state = {}
            for name, part in schematics.items():
                if name_conj in part["outputs"]:
                    state[name] = 0
            part_conj["state"] = state
    return schematics


schematics = parse_schematics(data)
print(schematics)
signal_queue = []


# Propagate signals:
# Filp parts: Ignore high signals, when get a low signal state flip. Send signal equal to new state to all outputs

# Conj parts: the status is the last signal received from each input. It updates when a new signal is received.
# If all inputs are high, send a low signal to all outputs. else it sends high.

# Broadcaster parts: Send the signal to all outputs

#Signal counter keep track of low and high signals
signal_counter = [0,0]
for i in range(1000):
    signal = {"target": "broadcaster", "state": 0, "sender": "button"}
    signal_queue.append(signal)
    while signal_queue:
        signal = signal_queue.pop(0)
        target = signal["target"]
        state = signal["state"]
        sender = signal["sender"]
        signal_counter[state] += 1
        if target not in schematics.keys():
            continue
        part = schematics[target]
        if part["type"] == "flip" and state == 0:
            part["state"] = not part["state"]
            for output in part["outputs"]:
                #print(target, int(part["state"]), "->", output)
                signal_queue.append({"target":output, "state": part["state"], "sender": target})
        elif part["type"] == "conj":
            part["state"][sender] = state
            if all(part["state"].values()):
                for output in part["outputs"]:
                    #print(target, "0", "->", output)
                    signal_queue.append({"target":output, "state": 0, "sender": target})
            else:
                for output in part["outputs"]:
                    #print(target, "1", "->", output)
                    signal_queue.append({"target":output, "state": 1, "sender": target})
        elif part["type"] == "brod":
            for output in part["outputs"]:
                #print(target, state, "->", output)
                signal_queue.append({"target":output, "state": state, "sender": target})


print(signal_counter)
score = signal_counter[0]*signal_counter[1]

puzzle.answer_a = score