#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
import numpy as np

DAY=17
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""


pattern = r'Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)'
matches = re.search(pattern, data)

register_a = matches.group(1)
register_b = matches.group(2)
register_c = matches.group(3)
program = matches.group(4)
program = program.split(",")
program = list(map(int, program))
memory = np.array([0,1,2,3,int(register_a),int(register_b),int(register_c)])
output=[]
ip = 0
def adv(param,ip):
    num = memory[4]
    div = 2**memory[param]
    memory[4] = num // div
    return ip+2

def bdv(param,ip):
    num = memory[4]
    div = 2**memory[param]
    memory[5] = num // div
    return ip+2

def cdv(param,ip):
    num = memory[4]
    div = 2**memory[param]
    memory[6] = num // div
    return ip+2

def bxl(param,ip):
    memory[5] = memory[5] ^ memory[param]
    return ip+2

def bst(param,ip):
    memory[5] = memory[param] % 8
    return ip+2

def jnz(param,ip):
    if memory[4] != 0:
        return memory[param]
    else:
        return ip+2

def bxc(param,ip):
    memory[5] = memory[5] ^ memory[6]
    return ip+2

def out(param,ip):
    output.append(memory[param]%8)
    return ip+2

def debug_print():
    print(f"ip={ip} {memory}")

while ip < len(program):
    instr = program[ip]
    param = program[ip+1]
    #print(instr)
    if instr == 0:
        ip = adv(param,ip)
        #debug_print()
    elif instr == 1:
        ip = bxl(param,ip)
        #debug_print()
    elif instr == 2:
        ip = bst(param,ip)
        #debug_print()
    elif instr == 3:
        ip = jnz(param,ip)
        #debug_print()
    elif instr == 4:
        ip = bxc(param,ip)
        #debug_print()
    elif instr == 5:
        ip = out(param,ip)
        #debug_print()
    elif instr == 6:
        ip = bdv(param,ip)
        #debug_print()
    elif instr == 7:
        ip = cdv(param,ip)
        #debug_print()
    else:
        print("Unknown instruction")
        break

print(output)
out_str= ",".join(map(str, output))

print(out_str)
#submit(out_str, part="a", day=DAY, year=2024, session=session_id)