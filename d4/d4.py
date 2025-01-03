'''Advent of Code 2020 - Day 4'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd4.txt'

class Passport: 
    def __init__(self):
        self.byr = None #birth year
        self.iyr = None #Issue year
        self.eyr = None #Expiration year
        self.hgt = None #Height
        self.hcl = None #Hair color
        self.ecl = None #Eye color
        self.pid = None #Passport ID
        self.cid = None #Country ID
        self.is_complete = False
    
    def _check_completeness(self):
        self.is_complete = all([self.byr, self.iyr, self.eyr, self.hgt,
                               self.hcl, self.ecl, self.pid])
    
    def update(self, line: str):
        
        args = line.split()
        for arg in args:
            param, val = arg.split(':')
        
            if param == 'byr':
                if len(val) == 4 and 1920 <= int(val) <= 2002: 
                    self.byr = val
            elif param == 'iyr':
                if len(val) == 4 and 2010 <= int(val) <= 2020: 
                    self.iyr = val  
            elif param == 'eyr':
                if len(val) == 4 and 2020 <= int(val) <= 2030:
                    self.eyr = val
            elif param == 'hgt':
                try:
                    dim = val[-2: ]
                    measure = int(val[: -2])
                    if (dim == 'cm' and 150 <= measure <= 193) or (dim == 'in' and 59 <= measure <= 76):
                        self.hgt = val
                except Exception as e:
                    print(e)
                    continue
            elif param == 'hcl':
                if val[0] == '#' and len(val) == 7 and val[1:7].isalnum():
                    self.hcl = val
            elif param == 'ecl':
                if val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    self.ecl = val
            elif param == 'pid':
                if len(val) == 9 and val.isdigit():
                    self.pid = val
            elif param == 'cid':
                self.param = val
        
        self._check_completeness()

complete = 0
with open(file_path, 'r') as f:
    passport = Passport()
    for line in f:
        line = line.strip()
        if line == '': 
            complete += 1 if passport.is_complete else 0
            passport = Passport()
        else: 
            passport.update(line)
            
print(f"Part one: {complete}")
