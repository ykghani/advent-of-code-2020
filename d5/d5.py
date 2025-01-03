'''Advent of Code 2020: Day 5'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd5.txt'

def bin_sort(instructions) -> int:
    low, high = 0, 128
    row, col = None, None 
    for ins in instructions[: 6]: 
        if ins == "F": #Case where you take the lower half of the range 
            high = (high - low) // 2 + low
        else:
            low = high - (high - low) // 2 
    
    if instructions[6] == 'F':
        row = low
    else:
        row = high - 1 
    
    low, high = 0, 8
    for ins in instructions[7:9]:
        if ins == 'L':
            high = (high - low) // 2 + low
        else:
            low = high - (high - low) // 2
    
    if instructions[9] == 'L':
        col = low
    else:
        col = high - 1

    return row * 8 + col             

# print(bin_sort('FBFBBFFRLR'))
max_id = 0
seat_ids = []
with open(file_path, 'r') as f: 
    for line in f: 
        seat_ids.append(bin_sort(line.strip()))
        if seat_ids[-1] > max_id:
            max_id = seat_ids[-1]

print(f"Part one: {max_id}")

seat_ids.sort()
part_two = None
for i in range(len(seat_ids) - 1):
    if seat_ids[i + 1] - seat_ids[i] == 2:
        part_two = seat_ids[i] + 1

print(f"Part two: {part_two}")