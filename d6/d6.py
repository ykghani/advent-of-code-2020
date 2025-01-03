'''Advent of Code 2020 Day 6'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd6.txt'

group_counts = 0
with open(file_path, 'r') as f: 
    answers = set()
    for line in f:
        line = line.strip()
        if line == '':
            group_counts += len(answers)
            answers = set()
        else:
            for char in line: 
                answers.add(char)
    
    group_counts += len(answers)

print(f"Part one: {group_counts}")

group_counts = 0
with open(file_path, 'r') as f: 
    responses = dict()
    group_size = 0
    for line in f: 
        line = line.strip()
        if line == '':
            group_counts += sum([1 for key in responses if responses[key] == group_size])
            responses = dict()
            group_size = 0
        else:
            group_size += 1
            for char in line:
                if char in responses: 
                    responses[char] +=  1
                else:
                    responses[char] = 1
    
    group_counts += sum([1 for key in responses if responses[key] == group_size])

print(f"Part two: {group_counts}")