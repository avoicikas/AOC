import pandas as pd
df = pd.read_csv('input3', header=None, names=['trial'])

df.head()

trial_length = len(df['trial'][0])


def count_trees(right, down):
    tree_count = 0
    i_right = 0
    i_down = down
    for index, row in df.iterrows():
        if index == i_down:
            i_down += down
            i_right += right
            i_right_adjusted = i_right % trial_length
            element = row['trial'][i_right_adjusted]
            if element == '#':
                tree_count += 1
    return tree_count

# task a


print(count_trees(3, 1))

#  task b
ans = 1
for right, down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    ans = ans * (count_trees(right, down))

print(ans)
