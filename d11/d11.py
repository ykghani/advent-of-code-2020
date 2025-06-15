'''Advent of Code 2020 Day 11 - Seating System'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd11.txt'

def get_neighbors(grid, y, x, part_one = False) -> list:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    if part_one: 
        return [(y + d[0], x + d[1]) for d in dirs if 0 <= y + d[0] < len(grid) and 0 <= x + d[1] < len(grid[0])]
    else:
        neighbors = []
        for dir in dirs:
            ny = y + dir[0]
            nx = x + dir[1]
            while in_grid(grid, ny, nx):
                if grid[ny][nx] == '#' or grid[ny][nx] == 'L':
                    neighbors.append((ny, nx))
                    break
                else:
                    ny += dir[0]
                    nx += dir[1]
        return neighbors

def in_grid(grid, y, x) -> bool:
    '''Returns if a point is in a grid or not'''
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def upgrade(grid, y, x):
    if grid[y][x] == 'L':
        grid[y][x] = '#'
    elif grid[y][x] == '#':
        grid[y][x] = 'L'
    
    return 

worthiness = []
def is_worthy(grid, y, x, neighbors, part_one= True):

    if grid[y][x] == 'L' and neighbors.count('#') == 0:
        return True 
    
    if part_one:     
        if grid[y][x] == '#' and neighbors.count('#') >= 4:
            return True
    else: 
        if grid[y][x] == '#' and neighbors.count('#') >= 5:
            return True
        
    return False


def check_grid(grid, part_one= False):
    updates = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            neighbors = [grid[n[0]][n[1]] for n in get_neighbors(grid, y, x, part_one)]
            if is_worthy(grid, y, x, neighbors, part_one):
                updates += 1
                worthiness.append((y, x))

    return updates 

def update_grid(grid, worthiness):
    for point in worthiness:
        upgrade(grid, point[0], point[1])
    

def occupied_seats(grid) -> int: 
    return sum(cell == '#' for row in grid for cell in row)            

def print_grid(grid):
    for row in grid: 
        print(''.join(row))
    return

grid = []

with open(file_path, 'r') as f: 
    grid = [list(line.strip()) for line in f]

answer = 0
part_one = False
while True:
    worthiness.clear()
    num_updates = check_grid(grid, part_one)
    
    if num_updates == 0: 
        answer = occupied_seats(grid)
        print(f"solution: {answer}")
        break
    else:
        update_grid(grid, worthiness)