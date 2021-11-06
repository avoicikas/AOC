with open('input11') as f:
    data = [list(x.strip()) for x in f.readlines()]

with open('testinput11') as f:
    testdata = [list(x.strip()) for x in f.readlines()]


def find_equilibruim(data):
    dat = [x[:] for x in data]
    has_changed = True
    w, h = len(dat), len(dat[0])
    while has_changed:
        has_changed = False
        old_dat = [x[:] for x in dat]
        for idy, elementy in enumerate(old_dat):
            for idx, elementx in enumerate(elementy):
                n = 0
                for dx, dy in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
                    if 0 <= dx+idx < h and 0 <= dy+idy < w:
                        if old_dat[idy+dy][idx+dx] == 'X':
                            n += 1
                if elementx == 'L' and n == 0:
                    dat[idy][idx] = 'X'
                    has_changed = True
                elif elementx == 'X' and n > 3:
                    dat[idy][idx] = 'L'
                    has_changed = True
    return dat


dd = find_equilibruim(testdata[:])
sum([l.count('X') for l in dd])

#  part 1

dd = find_equilibruim(data[:])
print(sum([l.count('X') for l in dd]))

# part 2


def find_equilibruim2(data):
    dat = [x[:] for x in data]
    has_changed = True
    w, h = len(dat), len(dat[0])
    while has_changed:
        has_changed = False
        old_dat = [x[:] for x in dat]
        for idy, elementy in enumerate(old_dat):
            for idx, elementx in enumerate(elementy):
                n = 0
                for dx, dy in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
                    iddx = dx+idx
                    iddy = dy+idy
                    while 0 <= iddx < h and 0 <= iddy < w:
                        if old_dat[iddy][iddx] == 'X':
                            n += 1
                        if old_dat[iddy][iddx] != '.':
                            break
                        iddx = iddx+dx
                        iddy = iddy+dy
                if elementx == 'L' and n == 0:
                    dat[idy][idx] = 'X'
                    has_changed = True
                elif elementx == 'X' and n > 4:
                    dat[idy][idx] = 'L'
                    has_changed = True
    return dat


dd = find_equilibruim2(testdata[:])
sum([l.count('X') for l in dd])

dd = find_equilibruim2(data[:])
print(sum([l.count('X') for l in dd]))
