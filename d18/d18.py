'''Advent of Code 2020 Day 18 - Operation Order'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd18.txt'

part_one = 0

def evaluate(input: str, i: int = 0) -> int:
    '''Takes a list of args from parsed expression string and evaluates as specified in problem'''
    result = 0
    op = "+"
    
    def apply_op(a, b, op):
        return a + b if op == "+" else a * b

    while i < len(input):
        char = input[i]
        if char == " ":
            i += 1
            continue
        elif char.isdigit():
            char = int(char)
            result = apply_op(result, char, op)
        elif char in "+*":
            op = char
        elif char == "(":
            num, i = evaluate(input, i + 1)
            result = apply_op(result, num, op)
        elif char == ")":
            return result, i
        i += 1
        
    return result, i

def evaluate_expression(input: str) -> int: 
    result, _ = evaluate(input)
    return result


with open(file_path, 'r') as f: 
    for line in f:
        part_one += evaluate_expression(line.strip())
        
print(f"Part one: {part_one}")