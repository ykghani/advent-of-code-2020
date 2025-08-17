'''Advent of Code 2020 Day 19 - Monster Messages'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd19_test.txt'

rules = {}
messages = []

with open(file_path, 'r') as f:
    for line in f: 
        line = line.strip()
        if line == "":
            continue
        elif ":" in line:
            args = line.split(":")
            rules[args[0].strip()] = args[1].strip()
        else:
            messages.append(line)

