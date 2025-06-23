'''Advent of Code 2020 Day 13 - Shuttle Search'''
from pathlib import Path
from functools import reduce

script_dir = Path(__file__).parent
file_path = script_dir / 'd13_text.txt'

from math import ceil

with open(file_path, 'r') as f: 
    EARLIEST_DEPARTURE = int(f.readline().strip())
    ALL_BUSSES = f.readline().strip().split(',')

valid_busses = [int(v) for v in ALL_BUSSES if v != 'x']
crt = {}
for idx, bus in enumerate(ALL_BUSSES):
    if bus != 'x':
        bus = int(bus)
        crt[bus] = idx

earliest_bus_id = None 
shortest_minutes_waited = 1e8

for bus in valid_busses:
    wait_time = (bus * ceil(EARLIEST_DEPARTURE / bus)) % EARLIEST_DEPARTURE
    if wait_time < shortest_minutes_waited:
        earliest_bus_id = bus
        shortest_minutes_waited = wait_time

print(f"{shortest_minutes_waited * earliest_bus_id}")

def modinv(a, m):
    # Returns x such that (a * x) % m == 1
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    # Returns a triple (g, x, y) such that a*x + b*y = g = gcd(a, b)
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

def chinese_remainder_theorem(remainders, moduli):
    M = reduce(lambda a, b: a * b, moduli)
    result = 0

    for ai, mi in zip(remainders, moduli):
        Mi = M // mi
        Ni = modinv(Mi, mi)
        result += ai * Mi * Ni

    return result % M

remainders = [(-offset) % bus for bus, offset in crt.items()]
moduli = list(crt.keys())
print(f"Part two: {chinese_remainder_theorem(remainders, moduli)}")