import pandas as pd
import re

#  task a

df = pd.read_csv('input5', header=None, names=["ticket"])


def get_row(row):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for element in row:
        if element == 'F':
            max_row = (max_row + min_row)//2
        elif element == 'B':
            min_row = round((max_row + min_row)/2)
        elif element == 'L':
            max_col = (max_col + min_col)//2
        elif element == 'R':
            min_col = round((max_col+min_col)/2)
    return max_row, max_col


get_row('FFFBBBFRRR')
get_row('BBFFBBFRLL')
get_row('FBFBBFFRLR')
get_row('FBFBBFBRLR')


df['RC'] = [get_row(x) for x in df['ticket']]


def get_id(row):
    return row[0]*8+row[1]


df['id'] = [get_id(x) for x in df['RC']]

df['id'].max()


def get_row_binary(row):
    row = re.sub('[FL]', '0', row)
    row = re.sub('[BR]', '1', row)
    return int(row, 2)


get_row_binary('BFFFBBFRRR')
get_id(get_row('BFFFBBFRRR'))

print(max(map(get_row_binary, df['ticket'])))

#  part b

rr = df.sort_values(by='id').reset_index(drop=True)
print(rr[rr['id'].diff() == 2]['id']-1)
