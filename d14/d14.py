'''Advent of Code 2020 Day 14 - Docking Data'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd14.txt'

memory = {}

def convert_to_36bit(value) -> list:
    '''Returns 36-bit string as list'''
    return list(format(int(value), '036b'))

def convert_to_int(value: list) -> int:
    '''Takes 36-bit list and returns the int value'''
    return int(''.join(value), 2)

def process_mask(mask: str, part_one = True) -> dict:
    '''Processes mask string and returns as dictionary of indices to update'''
    out = {}
    if part_one:
        for idx, char in enumerate(mask):
            if char != 'X':
                out[idx] = char
    else:
        for idx, char in enumerate(mask):
            if char == '1' or char == 'X':
                out[idx] = char
            
    return out    

def generate_addresses(masked):
    if 'X' not in masked:
        yield masked
    else:
        idx = masked.index('X')
        for bit in '01':
            masked[idx] = bit
            yield from generate_addresses(masked)
            masked[idx] = 'X'


def write_to_memory(mem_idx: int, mask: dict, value) -> None:
    '''Updates memory with value after mask is applied'''
    start_val = convert_to_36bit(value)
    for key, val in mask.items():
        start_val[key] = val
    memory[mem_idx] = convert_to_int(start_val)

def write_to_memory_part2(starting_mem_idx, mask: dict, value) -> None:
    '''PART 2 - Takes the starting mem idx to create the different mask permutations
    Those addresses are then updated with the original start value'''
    start_val = convert_to_36bit(starting_mem_idx)
    for key, val in mask.items():
        start_val[key] = val
    for address in generate_addresses(start_val):
        decimal_address = convert_to_int(address)
        memory[decimal_address] = int(value)

mask = {}
part_one = False
with open(file_path, 'r') as f: 
    for line in f:
        args = [arg.strip() for arg in line.split("=")]
        if args[0] == 'mask':
            mask = process_mask(args[-1], part_one)
        else:
            value = args[-1]
            mem_idx = args[0].split('[')[1].split(']')[0]
            if part_one:
                write_to_memory(mem_idx, mask, value)
            else:
                write_to_memory_part2(mem_idx, mask, value)

print(f"Part one: {sum([int(x) for x in memory.values()])}")