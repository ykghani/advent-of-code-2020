'''Advent of Code 2020 Day 3'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd3.txt'

grid = []
with open(file_path, 'r') as f:
    for line in f: 
        line = line.strip()
        grid.append(list(line))
        
def check_trees(grid, slope) -> int: 
    row_pos, col_pos = 0, 0
    row_dim, col_dim = len(grid), len(grid[0])
    trees = 0
    while row_pos < row_dim:
        trees += 1 if grid[row_pos][col_pos % col_dim] == '#' else 0
        row_pos += slope[0]
        col_pos += slope[1]
    
    return trees

slopes = [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)]

tree_encounters = 1
for slope in slopes: 
    tree_encounters *= check_trees(grid, slope)

print(f"Part two: {tree_encounters}")