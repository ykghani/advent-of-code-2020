'''Advent of Code 2020 Day 10 - Adapter Array'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd10.txt'

OUTLET = 0

with open(file_path, 'r') as f: 
    inp = f.readlines()
    
adapters = sorted(int(i.strip()) for i in inp)
built_in_adapter = max(adapters) + 3
adapters.append(built_in_adapter)

jolt_differential = {1: 0, 2: 0, 3: 0}
for idx, adapter in enumerate(adapters):
    if idx == 0:
        diff = adapter - OUTLET
    else:
        diff = adapter - adapters[idx - 1]
    
    jolt_differential[diff] += 1

print(jolt_differential)
print(f"Part 1: {jolt_differential[1] * jolt_differential[3]}")