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
        data = [x.strip().split(',') for x in f.readlines()]
        data=[int(x) for x in data[0]]
    return data

def open_file_df(file):
    df = pd.read_csv(file, header=None, names=[""])
    return df

def solve(data):
    final = []
    for test in range(np.max(data)):
        fuel = 0
        for number in data:
            fuel += np.abs(number - test)
        final.append(fuel)
    return np.min(final)

def solve2(data):
    final = []
    for test in range(np.max(data)):
        fuel = 0
        for number in data:
            for ii in range(1,np.abs(number - test)+1):
                fuel += ii
        final.append(fuel)
    return np.min(final)

def part1(file):
    data = open_file(file)
    result = solve(data)
    return result

def part2(file):
    data = open_file(file)
    result = solve2(data)
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
