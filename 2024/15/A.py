#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if r==0 and G[r][c]=='.':
            sr,sc = r,c

Q = deque([(0,sr,sc)])
SEEN = set()
while Q:
    d,r,c = Q.popleft()
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    if G[r][c]=='H':
        print(2*d)
        break
    for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
        rr,cc = r+dr,c+dc
        if 0<=rr<R and 0<=cc<C and G[r][c]!='#':
            Q.append((d+1, rr, cc))
