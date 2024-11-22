#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G = open(infile).read().strip()

segments = set()
leaves = set()
for line in G.split('\n'):
    x,y,z = 0,0,0
    steps = line.strip().split(',')
    for step in steps:
        d,amt = step[0], int(step[1:])
        dx,dy,dz = {'U': (0,1,0), 'D': (0,-1,0), 'R': (1,0,0), 'L': (-1,0,0), 'F': (0,0,1), 'B': (0,0,-1)}[d]
        for _ in range(amt):
            x,y,z = x+dx, y+dy, z+dz
            segments.add((x,y,z))
    leaves.add((x,y,z))

best = 10**20
for (sx,sy,sz) in segments:
    if sx==0 and sz==0:
        d = 0
        Q = deque([(0,sx,sy,sz)])
        SEEN = set()
        score = 0
        while Q:
            d,x,y,z = Q.popleft()
            if (x,y,z) in SEEN:
                continue
            SEEN.add((x,y,z))
            if (x,y,z) in leaves:
                score += d
            for dx,dy,dz in {'U': (0,1,0), 'D': (0,-1,0), 'R': (1,0,0), 'L': (-1,0,0), 'F': (0,0,1), 'B': (0,0,-1)}.values():
                xx,yy,zz = x+dx,y+dy,z+dz
                if (xx,yy,zz) in segments:
                    Q.append((d+1, xx, yy, zz))
        best = min(best, score)
print(best)
