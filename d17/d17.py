'''Advent of Code 2020 Day 17 - Conway Cubes'''
from pathlib import Path
from itertools import product

script_dir = Path(__file__).parent
file_path = script_dir / 'd17.txt'

NUM_ROUNDS = 6

with open(file_path, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
    height = len(lines)
    width = len(lines[0])

y_offset = height // 2
x_offset = width // 2

active_cells = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            active_cells.add((x - x_offset, y - y_offset, 0, 0))

def calc_bounding_box(coords: set) -> tuple:
    '''Returns the "bounding box" around the active cube based on active cells'''
    mins = tuple(min(v for v in axis) for axis in zip(*coords))
    maxs = tuple(max(v for v in axis) for axis in zip(*coords))
    return mins, maxs

def get_neighbors(x, y, z, w):
    for dx, dy, dz, dw in product([-1, 0, 1], repeat= 4):
        if dx == dy == dz == dw == 0:
            continue
        yield (x + dx, y + dy, z + dz, w + dw)

def requires_update(point: tuple, active_coords: set) -> bool:
    '''Checks if a point needs to be updated based on its neighbors'''
    x, y, z, w = point
    active_neighbors = sum(1 for n in get_neighbors(x, y, z, w) if n in active_coords)
    is_active = point in active_coords
    
    if is_active:
        return not (2 <= active_neighbors <= 3)
    else:
        return active_neighbors == 3

def update_cells(cells_to_update: list, current_active_cells: set) -> set:
    '''Returns new set of active cells based on inactive that need to become activated + cells that remain active'''
    return (current_active_cells - cells_to_update) | (cells_to_update - current_active_cells)

for _ in range(NUM_ROUNDS):
    staged_updates = set()
    
    mins, maxs = calc_bounding_box(active_cells)
    x_min, y_min, z_min, w_min = mins
    x_max, y_max, z_max, w_max = maxs
    
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for w in range(w_min - 1, w_max + 2):
                    if requires_update((x, y, z, w), active_cells):
                        staged_updates.add((x, y, z, w))
    
    active_cells = update_cells(staged_updates, active_cells)

print(f"Active cubes = {len(active_cells)}")