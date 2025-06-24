'''Advent of Code 2020 Day 17 - Conway Cubes'''
from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
file_path = script_dir / 'd17_test.txt'

cube = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

with open(file_path, 'r') as f:
    for line in f:
        line = list[line.strip()]