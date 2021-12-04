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
    return 1

def part1(file):
    data = open_file(file)
    result = solve(data)
    return result

def part2(file):
    data = open_file(file)
    result = solve(data)
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
