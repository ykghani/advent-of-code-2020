'''Advent of Code 2020 Day 12 - Rain Risk'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd12.txt'

coordinates = {'x': 0, 'y': 0, 'dir': 0}
waypoint_x = 10
waypoint_y = 1

directions = {0: 'east', 90: 'north', 180: 'west', 270: 'south'}
part_one = False

def part_two_rotate(x0, y0, xc, yc, action, degrees):
    '''
    Rotates the point (x0, y0) in a given direction around (xc, yc)
    For the sake of this problem, the SHIP will have coordinates (xc, yc)
    Returns the NEW coordinates of the waypoint post rotation
    '''
    
    from math import sin, cos, radians
    if action == 'R':
        degrees *= -1
    
    a = x0 - xc
    b = y0 - yc
    
    x1 = a * int(cos(radians(degrees))) - b * int(sin(radians(degrees))) + xc
    y1 = a * int(sin(radians(degrees))) + b * int(cos(radians(degrees))) + yc
    
    return int(x1), int(y1)

part_two_rotate(1, 0, 0, 0, "L", 90)
part_two_rotate(1, 0, 0, 0, 'R', 90)

with open(file_path, 'r') as f:
    for line in f: 
        line = line.strip()
        action = line[0]
        value = int(line[1:])
        
        if action == 'N':
            if part_one:
                coordinates['y'] += value
            else:
                waypoint_y += value
            
        elif action == 'S':
            if part_one:
                coordinates['y'] -= value
            else:
                waypoint_y -= value
                
        elif action == 'E':
            if part_one:
                coordinates['x'] += value
            else:
                waypoint_x += value
                
        elif action == 'W':
            if part_one:
                coordinates['x'] -= value
            else:
                waypoint_x -= value
                
        elif action == 'L':
            if part_one:
                coordinates['dir'] = (coordinates['dir'] + value) % 360
            else:
                waypoint_x, waypoint_y = part_two_rotate(waypoint_x, waypoint_y, coordinates['x'], coordinates['y'], action, value)
        elif action == 'R':
            if part_one:
                coordinates['dir'] = (coordinates['dir'] - value) % 360
            else:
                waypoint_x, waypoint_y = part_two_rotate(waypoint_x, waypoint_y, coordinates['x'], coordinates['y'], action, value)
        else:
            if part_one:
                if directions[coordinates['dir']] == 'east':
                    coordinates['x'] += value
                elif directions[coordinates['dir']] == 'north':
                    coordinates['y'] += value
                elif directions[coordinates['dir']] == 'west':
                    coordinates['x'] -= value
                else:
                    coordinates['y'] -= value
            else:
                wp_delta_x = waypoint_x - coordinates['x']
                wp_delta_y = waypoint_y - coordinates['y']
                coordinates['x'] += wp_delta_x * value
                coordinates['y'] += wp_delta_y * value
                waypoint_x = coordinates['x'] + wp_delta_x
                waypoint_y = coordinates['y'] + wp_delta_y
                

print(f"Answer: {abs(coordinates['x']) + abs(coordinates['y'])}")