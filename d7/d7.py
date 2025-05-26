'''Advent of Code Year 2020 - Day 7 Handy Haversacks'''
from pathlib import Path
from collections import defaultdict
import re

script_dir = Path(__file__).parent
file_path = script_dir / 'd7.txt'
all_bags = defaultdict(lambda: defaultdict(int))

pattern = r"^([\w\s]+) bags contain (.+)\.$"
contents_pattern = r"(\d+) ([\w\s]+) bags?"


def contains_bag(bags, outer_bag, target_bag) -> bool:
    if target_bag in bags[outer_bag]:
        return True
    
    for inner_bag in bags[outer_bag]:
        if contains_bag(bags, inner_bag, target_bag):
            return True
    
    return False

def bag_count(all_bags, color) -> int: 
    if color not in all_bags or len(all_bags[color]) == 0:
        return 0
    
    total = 0
    for inner_color, qty in all_bags[color].items():
        total += qty
        total += qty * bag_count(all_bags, inner_color)
    
    return total

with open(file_path, 'r') as f:
    for line in f:
        match = re.match(pattern, line)
        if match: 
            bag_color = match.group(1)
            contents_desc = match.group(2)
            
            if contents_desc == "no other bags":
                continue
            
            for contents_match in re.finditer(contents_pattern, contents_desc):
                quantity = int(contents_match.group(1))
                content_color = contents_match.group(2)
                
                all_bags[bag_color][content_color] = quantity

part_one_counter = 0
TARGET = 'shiny gold'
for bag in list(all_bags.keys()):
    if bag != TARGET and contains_bag(all_bags, bag, TARGET):
        part_one_counter += 1
        
print(part_one_counter)

print(bag_count(all_bags,TARGET))