from itertools import product

test_data = [
    '.#.',
    '..#',
    '###',
]

test_output = 112

with open('input17') as f:
    data = [(x.strip()) for x in f.readlines()]

directions = list(product((-1, 0, 1), repeat=3))
directions.remove((0, 0, 0))


def find_active(dat, rounds):
    l = len(dat)
    cube_active = {(x, y, 0) for x, l in enumerate(dat)
                   for y, c in enumerate(l) if c == "#"}
    for iround in range(rounds):
        temp_active = set()
        start = (iround+1) * -1
        stop = l + iround+1
        grid = product(range(start, stop), range(
            start, stop), range(start, stop))
        for x, y, z in grid:
            neighbors = sum(((x+dx, y+dy, z+dz) in cube_active)
                            for dx, dy, dz in directions)
            #  if neighbors > 1:
            if ((x, y, z) in cube_active and neighbors in (2, 3) or (x, y, z) not in cube_active and neighbors == 3):
                temp_active.add((x, y, z))
        cube_active = temp_active
    return len(cube_active)

#  part 1


find_active(data, 6)

#  part 2

directions = list(product((-1, 0, 1), repeat=4))
directions.remove((0, 0, 0, 0))


def find_active(dat, rounds):
    l = len(dat)
    cube_active = {(x, y, 0, 0) for x, l in enumerate(dat)
                   for y, c in enumerate(l) if c == "#"}
    for iround in range(rounds):
        temp_active = set()
        start = (iround+1) * -1
        stop = l + iround+1
        grid = product(range(start, stop), range(
            start, stop), range(start, stop), range(start, stop))
        for x, y, z, c in grid:
            neighbors = sum(((x+dx, y+dy, z+dz, c+dc) in cube_active)
                            for dx, dy, dz, dc in directions)
            if ((x, y, z, c) in cube_active and neighbors in (2, 3) or
                    (x, y, z, c) not in cube_active and neighbors == 3):
                temp_active.add((x, y, z, c))
        cube_active = temp_active
    return len(cube_active)


find_active(data, 6)
