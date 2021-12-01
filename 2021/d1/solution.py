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

def solve_part1(data):
    return np.sum(data.diff()>0)[0]

def solve_part2(data):
    return np.sum(np.diff(np.convolve(data.T.values[0],np.array([1,1,1]),mode='valid'))>0)


@ click.command()
@ click.option('--file', type=str, help='input filename', default='input')
def pipeline(file:str):
    data = open_file_df(file)
    result = solve_part1(data)
    print(result)
    result = solve_part2(data)
    print(result)


if __name__ == "__main__":
    pipeline()
