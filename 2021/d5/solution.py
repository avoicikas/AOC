import functools
import collections
import itertools
import math
from dataclasses import dataclass
import re
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.signal as signal
import scipy.stats as stats
import click
sns.set()

def open_file(file):
    with open(file) as f:
        data = [re.split(r' -> |,',x)for x in f.readlines()]
    data = pd.DataFrame(data,columns=['y1','x1','y2','x2'])
    data['y2'] = pd.to_numeric(data['y2'])
    data['x2'] = pd.to_numeric(data['x2'])
    data['y1'] = pd.to_numeric(data['y1'])
    data['x1'] = pd.to_numeric(data['x1'])
    return data


def solve(data):
    vent_map = np.zeros([1000,1000])
    for _, row in data.iterrows():
        if row['x1']==row['x2']:
            if row['y1']>row['y2']:
                b = row['y1']+1
                a = row['y2']
            else:
                a = row['y1']
                b = row['y2']+1
            vent_map[row['x1'],a:b]+=1
        elif row['y1']==row['y2']:
            if row['x1']>row['x2']:
                b = row['x1']+1
                a = row['x2']
            else:
                a = row['x1']
                b = row['x2']+1
            vent_map[a:b,row['y1']]+=1
    result = np.sum(vent_map>1)
    return result

def part1(file):
    data = open_file(file)
    result = solve(data)
    return result

def part2(file):
    data = open_file(file)
    result = solve2(data)
    return result

def solve2(data):
    vent_map = np.zeros([1001,1001])
    for _, row in data.iterrows():
        if row['x1']==row['x2']:
            if row['y1']>row['y2']:
                b = row['y1']+1
                a = row['y2']
            else:
                a = row['y1']
                b = row['y2']+1
            vent_map[row['x1'],a:b]+=1
        elif row['y1']==row['y2']:
            if row['x1']>row['x2']:
                b = row['x1']+1
                a = row['x2']
            else:
                a = row['x1']
                b = row['x2']+1
            vent_map[a:b,row['y1']]+=1
        else:
            if row['x1']<row['x2'] and row['y1']<row['y2']:
                y1,x1,y2,x2=row
                while x1<=x2:
                    vent_map[x1,y1]+=1
                    x1+=1
                    y1+=1
            elif row['x1']<row['x2'] and row['y1']>row['y2']:
                y1,x1,y2,x2=row
                while x1<=x2:
                    vent_map[x1,y1]+=1
                    x1+=1
                    y1-=1
            elif row['x1']>row['x2'] and row['y1']>row['y2']:
                y1,x1,y2,x2=row
                while x1>=x2:
                    vent_map[x1,y1]+=1
                    x1-=1
                    y1-=1
            elif row['x1']>row['x2'] and row['y1']<row['y2']:
                y1,x1,y2,x2=row
                while x1>=x2:
                    vent_map[x1,y1]+=1
                    x1-=1
                    y1+=1
    result = np.sum(vent_map>1)
    return result


@ click.command()
@ click.option('--file', type=str, help='input filename', default='input')
def main(file:str):
    result = part1(file)
    print(result)
    result = part2(file)
    print(result)


if __name__ == "__main__":
    main()
