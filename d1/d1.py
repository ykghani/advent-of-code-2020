'''Advent of Code 2020 - Day 1'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd1.txt'

with open(file_path, 'r') as f:
    vals = [int(line.strip()) for line in f]

for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        if vals[i] + vals[j] == 2020:
            print(f"Part one: {vals[i] * vals[j]}")

for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        for k in range(j + 1, len(vals)):
            if vals[i] + vals[j] + vals[k] == 2020:
                print(f"Part two: {vals[i] * vals[j] * vals[k]}")