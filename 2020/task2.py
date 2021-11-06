import pandas as pd
df = pd.read_csv('input2.txt', sep=' ', header=None,
                 names=['limits', 'letter', 'string'])

# task a

df['letter'] = df['letter'].str.replace(':', '')
df['limits'] = df['limits'].str.split('-')
df.head()

valid = 0
for index, row in df.iterrows():
    real_count = row['string'].count(row['letter'])
    if real_count >= pd.to_numeric(row['limits'][0]) and real_count <= pd.to_numeric(row['limits'][1]):
        valid += 1

print(valid)

# task b

valid = 0
for index, row in df.iterrows():
    if row['string'][pd.to_numeric(row['limits'][0])-1] == row['letter']:
        if row['string'][pd.to_numeric(row['limits'][1])-1] != row['letter']:
            valid += 1
    if row['string'][pd.to_numeric(row['limits'][0])-1] != row['letter']:
        if row['string'][pd.to_numeric(row['limits'][1])-1] == row['letter']:
            valid += 1

print(valid)
