'''Advent of Code 2020 Day 15 - Rambunctious Recitation'''
from collections import defaultdict, deque

INPUT = [2, 0, 1, 9, 5, 19]
ROUNDS = 30000000

last_spoken_tracker = defaultdict(lambda: deque([], maxlen= 2))

talk_track = []
for round in range(1, ROUNDS + 1):
    if round < len(INPUT) + 1:
        last_spoken_tracker[INPUT[round - 1]].appendleft(round)
        talk_track.append(INPUT[round - 1])
    else:
        if len(last_spoken_tracker[talk_track[-1]]) < 2:
            talk_track.append(0)
            last_spoken_tracker[0].appendleft(round)
        else:
            delta = last_spoken_tracker[talk_track[-1]][0] - last_spoken_tracker[talk_track[-1]][1]
            talk_track.append(delta)
            last_spoken_tracker[delta].appendleft(round)

print(talk_track[-1])