from sympy.ntheory.modular import solve_congruence
import re
import numpy as np
with open('input13') as f:
    data = [(x.strip()) for x in f.readlines()]

timestamp = int(data[0])
bus_numbers = [int(x) for x in re.findall(r'(\d+)', data[1])]

departure_times = [(x-timestamp % x) for x in bus_numbers]
minimum = np.argmin(departure_times)

#  part 1

print(departure_times[minimum]*bus_numbers[minimum])

# part 2

offsets = []
for idx, element in enumerate(data[1].split(',')):
    if element != 'x':
        offsets.append(idx)

offsets = np.array(offsets)
bus_numbers = np.array(bus_numbers)

offsets
bus_numbers


def search_bus(bus_numbers, offsets):
    not_found = True
    timestamp_mult = round(500000000000000/13)
    while not_found:
        newstamp = (bus_numbers[0]*timestamp_mult)
        if (newstamp+offsets[1]) % bus_numbers[1] == 0:
            for idx, element in enumerate(offsets[1:]):
                if (newstamp+element) % bus_numbers[idx+1] != 0:
                    break
            else:
                not_found = False
        timestamp_mult += 1
    return newstamp


# super slow brute force
#  print(search_bus(bus_numbers[:], offsets[:]))


#  with sympy

bus_times = [(-i, int(x))
             for i, x in enumerate(data[1].split(',')) if x != 'x']
_, busses = zip(*bus_times)

print(solve_congruence(*bus_times)[0])
