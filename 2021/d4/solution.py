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
    numbers = [int(x) for x in data[0].split(',')]
    all_puzles = []
    puzle= []
    for line in data[2:]:
        if line=='':
            all_puzles.append(puzle)
            puzle = []
        else:
            puzle.append([int(x) for x in line.split(' ') if x != ''])
    all_puzles.append(puzle)
    return numbers, all_puzles

def solve_board(numbers, board):
    numbers = np.array(numbers)
    max_index = []
    possible = False
    for row in board:
        possible=np.all([x in numbers for x in row])
        if possible:
            max_index.append(np.max([np.where(x==numbers)[0][0] for x in row]))
    for row in np.array(board).T:
        possible=np.all([x in numbers for x in row])
        if possible:
            max_index.append(np.max([np.where(x==numbers)[0][0] for x in row]))
    return possible, min(max_index)

def solve(numbers, all_boards):
    solution_time = []
    solution_board = []
    for idx, board in enumerate(all_boards):
        possible, max_index = solve_board(numbers, board)
        if possible:
            solution_time.append(max_index)
            solution_board.append(idx)
    win_board = solution_board[np.argmin(solution_time)]
    wining_number = numbers[np.min(solution_time)]
    wining_board = np.array(all_boards[win_board][:]).ravel()
    for inmbr in numbers[:np.min(solution_time)+1]:
        wining_board=np.delete(wining_board,np.where(wining_board==inmbr))
    return wining_number * np.sum(wining_board)

def solve2(numbers, all_boards):
    solution_time = []
    solution_board = []
    for idx, board in enumerate(all_boards):
        possible, max_index = solve_board(numbers, board)
        if possible:
            solution_time.append(max_index)
            solution_board.append(idx)
    win_board = solution_board[np.argmax(solution_time)]
    wining_number = numbers[np.max(solution_time)]
    wining_board = np.array(all_boards[win_board][:]).ravel()
    for inmbr in numbers[:np.max(solution_time)+1]:
        wining_board=np.delete(wining_board,np.where(wining_board==inmbr))
    return wining_number * np.sum(wining_board)

def part1(file:str):
    numbers, all_boards = open_file(file)
    result = solve(numbers, all_boards)
    return result

def part2(file:str):
    numbers, all_boards = open_file(file)
    result = solve2(numbers, all_boards)
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
