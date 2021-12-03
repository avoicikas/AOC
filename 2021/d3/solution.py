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

def solve(df):
    answer = 0
    ll=len(df)/2
    for i,row in df.iterrows():
        answer+=np.array([int(x) for x in row[0]])
    a=[str(int(x)) for x in answer<ll]
    b=[str(int(x)) for x in answer>ll]
    a = ''.join(a)
    b = ''.join(b)
    return int(a,2)*int(b,2)

def get_bigger_numbers(df,bitnumber,more:bool):
    answer = 0
    ll=len(df)/2
    for i,row in df.iterrows():
        answer+=np.array([int(x) for x in row[0]])
    if more:
        if answer[bitnumber]==ll:
            b=1
        else:
            b=[int(x) for x in answer>=ll][bitnumber]
    else:
        if answer[bitnumber]==ll:
            b=0
        else:
            b=[int(x) for x in answer<=ll][bitnumber]
    result=[]
    for i,row in df.iterrows():
        if np.array([int(x) for x in row[0]])[bitnumber]==b:
            result.append(row[0])
    return pd.DataFrame(result)


def solve_part2(dd):
    df = dd.copy()
    for ii in range(12):
        df=get_bigger_numbers(df,ii,1)
        if len(df)==1:
            break
    a = df[0]
    df = dd.copy()
    for ii in range(12):
        df=get_bigger_numbers(df,ii,0)
        if len(df)==1:
            break
    b = df[0]
    return int(a[0],2)*int(b[0],2)

@ click.command()
@ click.option('--file', type=str, help='input filename', default='input')
def pipeline(file:str):
    data = open_file(file)
    dd = pd.DataFrame(data)
    result = solve(dd)
    print(result)
    result = solve_part2(dd)
    print(result)

if __name__ == "__main__":
    pipeline()
