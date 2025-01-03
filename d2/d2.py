'''Advent of Code 2020 Day 2'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd2.txt'

def parse_line(line):
    pass_range, policy, password = line.strip().split()
    
    pass_low, pass_high = pass_range.split('-')
    policy = policy[0]
    
    return (int(pass_low), int(pass_high)), policy, password

def check_validity(lims, policy, password) -> bool: 
    return lims[0] <= password.count(policy) <= lims[1]

def part_two_validity(lims, policy, password) -> bool:
    return (password[lims[0] - 1] == policy) ^ (password[lims[1] - 1] == policy)

ans = 0
is_part_one = False
with open(file_path, 'r') as f: 
    if is_part_one:
        ans = sum([check_validity(*parse_line(line)) for line in f])
    else: 
        ans = sum([part_two_validity(*parse_line(line)) for line in f])
    
print(f"Part one flag: {is_part_one}, ans: {ans}")