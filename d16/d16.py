'''Advent of Code 2020 Day 16 - Ticket Translation'''
from pathlib import Path
import re

script_dir = Path(__file__).parent
file_path = script_dir / 'd16.txt'

field_pattern = re.compile(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

fields_dict = {}
my_ticket = []
other_tickets = []

mode = "fields"
with open(file_path, 'r') as f: 
    for line in f: 
        line = line.strip()
        if line  == "":
            continue
        elif line == "your ticket:":
            mode = "your_ticket"
            continue
        elif line == "nearby tickets:":
            mode = "nearby_tickets"
            continue
        if mode == 'fields':
            match = field_pattern.match(line)
            if match:
                field = match.group(1)
                range1 = (int(match.group(2)), int(match.group(3)))
                range2 = (int(match.group(4)), int(match.group(5)))
                fields_dict[field] = (range1, range2)
        elif mode == 'your_ticket':
            my_ticket = list(map(int, line.split(',')))
        else:
            other_tickets.append(list(map(int, line.split(','))))

all_tickets = [my_ticket] + other_tickets

def in_range(val: int, ranges: list) -> bool:
    '''Checks if a value is within one of the ranges associated with a field'''
    for a_range in ranges:
        if a_range[0] <= val <= a_range[1]:
            return True
    return False

def check_ticket_validity(ticket: list, rules: dict):
    '''Checks if a ticket is valid. Returns integer value that is not valild for any field or 0 if valid'''
    invalid_value = 0
    for number in ticket:
        if not any(in_range(number, rule) for rule in rules.values()):
            invalid_value = number
    return invalid_value

part_one = 0
valid_tickets = []
for tic in all_tickets:
    value = check_ticket_validity(tic, fields_dict)
    part_one += value
    if value == 0:
        valid_tickets.append(tic)
        
print(f"Part 1: {part_one}")

###PART TWO###

def field_matches_values(values: list, ranges: list[tuple[int, int]]) -> bool:
    return all(in_range(val, ranges) for val in values)

def find_matching_fields(attribute_values: list, fields_dict: dict, valid_fields=None) -> list:
    '''Returns list of matching fields for a given attribute'''
    matching_fields = []
    if valid_fields is None:
        valid_fields = list(fields_dict.keys())

    for field in valid_fields:
        if field_matches_values(attribute_values, fields_dict[field]):
            matching_fields.append(field)

    return matching_fields

attributes = [[attr[i] for attr in valid_tickets] for i in range(len(valid_tickets[0]))] #attribute 0 will be 0th element in all tickets

field_mapping = {}
part_two = 1
valid_fields = list(fields_dict.keys())
while len(field_mapping) < len(fields_dict):
    for idx, attr in enumerate(attributes):
        if idx in field_mapping.values(): 
            continue
        potential_fields = find_matching_fields(attr, fields_dict, valid_fields)
        if len(potential_fields) == 1: #only 1 match, must be that attribute!
            key = potential_fields[0]
            field_mapping[key] = idx
            if 'departure' in key:
                part_two *= my_ticket[idx]
            valid_fields.remove(key)

print(f"Part two: {part_two}")