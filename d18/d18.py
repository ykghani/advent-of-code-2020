'''Advent of Code 2020 Day 18 - Operation Order'''
from pathlib import Path
import re 

script_dir = Path(__file__).parent
file_path = script_dir / 'd18.txt'

part_one = part_two = 0

def tokenize(expr):
    '''Returns a list of tokens, including parentheses and operators'''
    return re.findall(r'\d+|[()+*]', expr)

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


def eval_tokens(tokens):
    def eval_inner(i):
        values = []
        ops = []

        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                val, i = eval_inner(i + 1)
                values.append(val)
            elif token == ')':
                break
            elif token in '+*':
                ops.append(token)
            else:
                values.append(int(token))
            i += 1

        # First resolve all additions
        j = 0
        while '+' in ops:
            if ops[j] == '+':
                res = values[j] + values[j + 1]
                values = values[:j] + [res] + values[j + 2:]
                ops.pop(j)
            else:
                j += 1

        result = values[0]
        for k, op in enumerate(ops):
            if op == '*':
                result *= values[k + 1]
        return result, i

    result, _ = eval_inner(0)
    return result

def eval_expr_custom_precedence(expr: str) -> int:
    tokens = tokenize(expr)
    return eval_tokens(tokens)

with open(file_path, 'r') as f: 
    for line in f:
        part_one += evaluate_expression(line.strip())
        part_two += eval_expr_custom_precedence(line.strip())
        
print(f"Part one: {part_one}")
print(f"Part two: {part_two}")