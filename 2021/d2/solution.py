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
        data = [(x.strip()) for x in f.readlines()]
    return data

def open_file_df(file):
    df = pd.read_csv(file, header=None, names=[""])
    return df

def solve(data):
    depth = 0
    distance = 0
    for element in data:
        if element.startswith('f'):
            distance = distance + int(element[-1])
        elif element.startswith('d'):
            depth = depth+int(element[-1])
        elif element.startswith('u'):
            depth = depth-int(element[-1])
    return depth*distance

def solve_part2(data):
    depth = 0
    distance = 0
    aim = 0
    for element in data:
        if element.startswith('f'):
            distance = distance + int(element[-1])
            depth = depth + aim*int(element[-1])
        elif element.startswith('d'):
            aim = aim+int(element[-1])
        elif element.startswith('u'):
            aim = aim-int(element[-1])
    return depth*distance

@ click.command()
@ click.option('--file', type=str, help='input filename', default='input')
def pipeline(file:str):
    data = open_file(file)
    result = solve(data)
    print(result)
    result = solve_part2(data)
    print(result)


if __name__ == "__main__":
    pipeline()
