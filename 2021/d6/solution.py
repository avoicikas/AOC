import functools
from scipy.optimize import curve_fit
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
import numba
sns.set()

def open_file(file):
    with open(file) as f:
        data = [int(x) for x in re.findall(r'\d+',f.read().strip())]
    return data

def func(a, b, t):
    return a+b*np.log(t)

def solve(data,days=80):
    for _ in range(days):
        new_fish = 0
        for idx, fish in enumerate(data):
            if fish ==0:
                new_fish+=1
                data[idx]=7
        data = [x-1 for x in data]
        for _ in range(new_fish):
            data.append(8)
    return len(data)

def solve2(data, days=256):
    # count all types of fish to cycle them in groups
    data = [data.count(x) for x in [0,1,2,3,4,5,6,7,8]]
    for i in range(days):
        data[(i + 7) % 9] += data[i % 9]
    return sum(data)

def part1(file):
    data = open_file(file)
    result = solve(data)
    return result

def part2(file,days=256):
    data = open_file(file)
    result = solve2(data,days=days)
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
