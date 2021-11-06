import numpy as np
df = np.loadtxt("data1.csv")
df = set(df)
# task 1 a
print([a * (2020 - a) for a in df if 2020 - a in df][0])

# task 1 b
print([a * b * (2020 - a - b)
       for a in df for b in df if 2020 - a - b in df][0])
