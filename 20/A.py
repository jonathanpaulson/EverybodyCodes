#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
from copy import deepcopy
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c

Q = deque([])
for d in range(4):
    Q.append([0, sr, sc, 1000, d])

SEEN = set()
best = 0
while Q:
    d, r, c, z, dir_ = Q.popleft()
    if d==100:
        best = max(best, z)
        continue
    if (r,c,z,dir_) in SEEN:
        continue
    SEEN.add((r,c,z,dir_))
    for ddir in [3, 0, 1]:
        new_dir = (dir_ + ddir)%4
        dr,dc = [(-1,0), (0, 1), (1, 0), (0, -1)][new_dir]
        rr = r+dr
        cc = c+dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
            if G[rr][cc] in ['.', 'S']:
                new_z = z-1
            elif G[rr][cc] == '-':
                new_z = z-2
            elif G[rr][cc] == '+':
                new_z = z+1
            else:
                assert False
            Q.append((d+1, rr, cc, new_z, new_dir))
print(best) 
        
