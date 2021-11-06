from collections import defaultdict
import numpy as np
with open('input10') as f:
    data = [int(x) for x in f.readlines()]

len(data)

test_data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
             45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

dd_test = test_data[:] + [0] + [np.max(test_data)+3]
np.multiply.reduce(np.unique(np.diff(sorted(dd_test)), return_counts=True)[1])

#  part 1

dd = data[:] + [0] + [np.max(data)+3]
np.multiply.reduce(np.unique(np.diff(sorted(dd)), return_counts=True)[1])

# part 2

dd = [0] + sorted(data[:]) + [np.max(data)+3]

paths = defaultdict(int)
paths[0] = 1
for i in range(1, len(dd)):
    for j in range(i)[::-1]:
        if dd[i] - dd[j] > 3:
            break
        paths[i] += paths[j]

print(paths[len(dd)-1])
