import re
import pandas as pd

with open('input4') as f:
    data = f.read()

passports = []
for ipass in data.split('\n\n'):
    parsedpass = re.findall(r'(\w+):(\S+)', ipass)
    passports.append({x[0]: x[1] for x in parsedpass})

df = pd.DataFrame(passports)
df = df.drop('cid', axis=1)
df = df.dropna()
# part a

print(df.shape[0])

# part b
df['byr'] = pd.to_numeric(df['byr'])
df['iyr'] = pd.to_numeric(df['iyr'])
df['eyr'] = pd.to_numeric(df['eyr'])

dff = df[(df['byr'] >= 1920) & (df['byr'] <= 2002)]
dff = dff[(dff['iyr'] >= 2010) & (dff['iyr'] <= 2020)]
dff = dff[(dff['eyr'] >= 2020) & (dff['eyr'] <= 2030)]


def bad_hgt(row):
    height = re.match(r'(\d+)(cm|in)', row['hgt'])
    try:
        height, unit = height[1], height[2]
    except:
        unit = ''
    if unit == 'cm':
        if not 150 <= int(height) <= 193:
            return False
    elif unit == 'in':
        if not 59 <= int(height) <= 76:
            return False
    else:
        return False
    return(True)


dff = dff[dff.apply(bad_hgt, axis=1)]


def bad_hcl(row):
    if row['hcl'][0] != '#' or len(row['hcl']) != 7:
        return False
    return True


dff = dff[dff.apply(bad_hcl, axis=1)]

dff = dff[dff.apply(lambda x: x['ecl'] in ['amb', 'blu',
                                           'brn', 'gry', 'grn', 'hzl', 'oth'], axis=1)]


dff = dff[dff.apply(lambda x: len(x['pid']) == 9, axis=1)]

dff.shape[0]
