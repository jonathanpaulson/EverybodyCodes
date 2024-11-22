#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()

height = 0
best = 0
steps = G.split(',')
for step in steps:
    d,amt = step[0], int(step[1:])
    if d=='U':
        height += amt
        best = max(best, height)
    elif d=='D':
        height -= amt
        best = max(best, height)
print(best)
