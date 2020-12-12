with open('input12') as f:
    data = [(x.strip()) for x in f.readlines()]

data = [(x[0], int(x[1:])) for x in data]

directions = {'N': 1j, "E": 1, 'W': -1, 'S': -1j}
rotations = {'R': -1j, 'L': 1j}

location = 0
direction = 1

for command, number in data:
    if command in directions:
        location += directions[command]*number
    elif command in rotations:
        direction *= rotations[command] ** (number/90)
    else:
        location += direction * number

#  part 1

print(abs(location.real)+abs(location.imag))

#  part 2

location = 0
direction = 10+1j

for command, number in data:
    if command in directions:
        direction += directions[command]*number
    elif command in rotations:
        direction *= rotations[command] ** (number/90)
    else:
        location += direction * number

print(abs(location.real)+abs(location.imag))
