'''Advent of Code 2020 Day 9 - Encoding Error'''
from pathlib import Path
from itertools import combinations

script_dir = Path(__file__).parent
file_path = script_dir / 'd9.txt'

with open(file_path, 'r') as f: 
    lines = f.readlines()


class Preamble:
    def __init__(self, lines, preamble_len= 25):
        self.preamble = [int(i.strip()) for i in lines[:preamble_len]]
        self.vals = [int(i.strip()) for i in lines[preamble_len:]]
        self.all_vals = self.preamble + self.vals
        self.oldest = self.preamble[0]
        self.combos = list(combinations(self.preamble, 2))
        self.checksums = [sum(combo) for combo in self.combos]
        self.idx = 0
        self.preamble_len = len(self.preamble)
        self.part_one_val = None
        self.part_one_idx = 0

    def update(self):
        self.combos = [pair for pair in self.combos if self.oldest not in pair]
        

        self.preamble.append(self.vals[self.idx])
        self.idx += 1
        self.preamble = self.preamble[1: ]
        self.oldest = self.preamble[0]
        latest = self.preamble[-1]
        
        self.combos.extend([(val, latest) for val in self.preamble[0: self.preamble_len - 1]])
        self.checksums = [sum(combo) for combo in self.combos]
        return 
    
    def is_valid(self) -> bool:
        return self.vals[self.idx] in self.checksums
    
    def execute(self):
        while self.idx < len(self.vals):
            if not self.is_valid():
                self.part_one_val = self.vals[self.idx]
                self.part_one_idx = self.idx
                return
            else:
                self.update()
    
    def contiguous_sum(self):
        for start in range(0, self.part_one_idx):
            for end in range(0, self.part_one_idx):
                if sum(self.all_vals[start: end]) == self.part_one_val:
                    return min(self.all_vals[start: end]) + max(self.all_vals[start: end])

preamble = Preamble(lines)
preamble.execute()
print(preamble.part_one_val)
print(preamble.contiguous_sum())