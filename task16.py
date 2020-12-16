from scipy.sparse.csgraph import maximum_bipartite_matching
from scipy.sparse import csr_matrix
import numpy as np

with open('input16') as f:
    data = [(x.strip()) for x in f.readlines()]

memory_range = []
for irange in data[:20]:
    memory_range.append(re.findall(r'\d+', irange))

min_value = int(min(min(memory_range)))
max_value = int(max(max(memory_range)))

numbers = []
for ticket in data[25:]:
    numbers.extend([int(x) for x in (re.findall(r'\d+', ticket)) if int(x) < min_value
                    or int(x) > max_value])

#  part 1

print(sum(numbers))

# part 2

#  discard bad
valid_tickets = []
for ticket in data[25:]:
    numbers = [int(x) for x in (re.findall(r'\d+', ticket))
               if int(x) < min_value or int(x) > max_value]
    if len(numbers) == 0:
        valid_tickets.append([int(x) for x in (re.findall(r'\d+', ticket))])

nearby = np.array(valid_tickets)
ranges = np.array(memory_range).astype(int)
mine = np.array([int(x) for x in data[22].split(',')], dtype=np.int64)

# ticket column vs range
fit_in_range = [[all((t1 <= l[j] <= t2) or (t3 <= l[j] <= t4) for l in nearby)
                 for t1, t2, t3, t4 in ranges]
                for j in range(20)]


sorted_ranges = maximum_bipartite_matching(csr_matrix(fit_in_range))
print(mine[sorted_ranges[:6]].prod())

pd.DataFrame(fit_in_range)
