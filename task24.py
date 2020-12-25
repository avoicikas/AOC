import re

with open('input24') as f:
    ls = [line.strip() for line in f.readlines()]

ds = {'e':  2, 'se':  1 - 1j, 'sw': -1 - 1j,
      'w': -2, 'nw': -1 + 1j, 'ne':  1 + 1j}

# Part one
black = set()
for l in ls:
    dirs = re.findall('e|se|sw|w|nw|ne', l)
    z = sum(ds[d] for d in dirs)
    if z in black:
        black.remove(z)
    else:
        black.add(z)

print(len(black))

# Part two
for i in range(100):
    new_black = set()
    to_check = {z + s for s in ds.values() for z in black}
    for t in to_check:
        adj = sum(t + s in black for s in ds.values())
        if (t in black and 1 <= adj <= 2) or (t not in black and adj == 2):
            new_black.add(t)
    black = new_black

print(len(black))
