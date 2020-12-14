import rje
from itertools import product
from collections import defaultdict

with open('input14') as f:
    data = [(x.strip()) for x in f.readlines()]


def set_bit(number, mask):
    number = bin(number)[2:].zfill(len(mask))
    ans = []
    for index, element in enumerate(mask):
        if element != 'X':
            ans.append(element)
        else:
            ans.append(number[index])
    return int(''.join(ans))


def run_program(dat):
    memory = {}
    for element in dat:
        if element[0:2] == 'ma':
            mask = element[7:]
        elif element[0:2] == 'me':
            mem_loc = int(re.findall(r'mem\[(\d+)\]', element)[0])
            mem_value = int(re.findall(r'= (\d+)', element)[0])
            memory[mem_loc] = set_bit(mem_value, mask)
    return sum([int(str(x), 2) for x in memory.values()])

#  part 1


run_program(data)

#  part 2


def set_bit2(number, mask):
    number = bin(number)[2:].zfill(len(mask))
    ans = []
    for index, element in enumerate(mask):
        if element != '0':
            ans.append(element)
        else:
            ans.append(number[index])
    return ans


def expand(x_lock):
    xs = [i for i, x in enumerate(x_lock) if x == 'X']
    for rep in product(['0', '1'], repeat=len(xs)):
        new_lock = list(x_lock)
        for i, new_val in zip(xs, rep):
            new_lock[i] = new_val
        yield new_lock


def run_program2(dat):
    memory = {}
    for element in dat:
        if element[0:2] == 'ma':
            mask = element[7:]
        elif element[0:2] == 'me':
            mem_loc = int(re.findall(r'mem\[(\d+)\]', element)[0])
            mem_value = int(re.findall(r'= (\d+)', element)[0])
            newloc = set_bit2(mem_loc, mask)
            for newl in expand(newloc):
                loc = int(''.join(newl), 2)
                memory[loc] = mem_value
    return sum([x for x in memory.values()])


run_program2(data)
