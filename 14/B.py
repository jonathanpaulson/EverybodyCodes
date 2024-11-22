#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()

ans = set()
for line in G.split('\n'):
    x,y,z = 0,0,0
    steps = line.strip().split(',')
    for step in steps:
        d,amt = step[0], int(step[1:])
        dx,dy,dz = {'U': (0,1,0), 'D': (0,-1,0), 'R': (1,0,0), 'L': (-1,0,0), 'F': (0,0,1), 'B': (0,0,-1)}[d]
        for _ in range(amt):
            x,y,z = x+dx, y+dy, z+dz
            ans.add((x,y,z))
print(len(ans))
