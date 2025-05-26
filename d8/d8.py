'''Advent of Code 2020 Day 8 - Handheld Halting'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd8_test.txt'

class Console:
    def __init__(self, file_path):
        self.accumulation = 0
        self.pos = 0
        with open(file_path, 'r') as f: 
            self.original_instructions = f.read().splitlines()
        self.instructions = self.original_instructions.copy()
        
        self.processed_instructions = []
        self.working_instructions = []
        self.ops = {
            'acc': self._acc,
            'jmp': self._jmp,
            'nop': self._nop
        }
        
        self.changed_ops = []
        self.last_changed_op_pos = 0
    
    def _nop(self, *args):
        self.pos += 1
        return
    
    def _acc(self, *args):
        val = int(args[0])
        self.accumulation += val
        self.pos += 1
    
    def _jmp(self, *args):
        offset = int(args[0])
        self.pos += offset
    
    def execute(self, part_two= False):
        while True:
            if self.pos in self.processed_instructions:
                if part_two: 
                    return 'INFINITE_LOOP'
                else:
                    self.reset()
                    return self.accumulation
            else:
                params = self.working_instructions[self.pos].split()
                operation = params[0]
                arguments = params[1:]
                
                self.processed_instructions.append(self.pos)
                self.ops[operation](*arguments)
            
            if self.pos == len(self.working_instructions) - 1 and len(self.processed_instructions) == len(self.working_instructions):
                return self.accumulation
    
    def update_working_instructions(self, debug = False):
        '''Finds next op to change and creates new set of working instructions'''
        working_instructions = self.instructions.copy()
        if debug:
            i = 7
            params = working_instructions[i].split()
            if params[0] == 'nop':
                working_instructions[i] = f'jmp {params[1]}'
            else:
                working_instructions[i] = f'nop {params[1]}'
        
            self.working_instructions = working_instructions
            self.last_changed_op_pos = i + 1
            return
            
        for i in range(self.last_changed_op_pos, len(self.instructions)):
            params = working_instructions[i].split()
            if params[0] == 'acc':
                continue
            else:
                if params[0] == 'nop':
                    working_instructions[i] = f'jmp {params[1]}'
                else:
                    working_instructions[i] = f'nop {params[1]}'
                
            self.working_instructions = working_instructions
            self.last_changed_op_pos = i + 1
            return
        
    def reset(self):
        self.pos = 0
        self.accumulation = 0
        self.working_instructions = []
        self.processed_instructions = []
        self.instructions = self.original_instructions.copy()
        
    
    def part_two(self): 
        while self.last_changed_op_pos < len(self.instructions):
            self.update_working_instructions()
            if self.execute(part_two= True) == 'INFINITE_LOOP':
                self.reset()
                continue
            else:
                return self.accumulation
             

console = Console(file_path)
part_one = console.execute()
print(f"Part one: {part_one}")
console.reset()
part_two = console.part_two()
print(f"Part two: {part_two}")