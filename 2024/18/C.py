#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

def getDistances(sr,sc):
    ret = {}
    Q = deque([(0,sr,sc)])
    SEEN = set()
    score = 0
    while Q:
        d,r,c = Q.popleft()
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        if G[r][c] == '.':
            ret[(r,c)] = d
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[r][c]!='#':
                Q.append((d+1, rr, cc))
    return ret

opts = []
palms = set()
for r in range(R):
    for c in range(C):
        if G[r][c] == '.':
            opts.append((r,c))
        if G[r][c] == 'P':
            palms.add((r,c))

D = []
for (r,c) in palms:
    D.append(getDistances(r,c))
best = 10**9
for (r,c) in opts:
    score = sum(d[(r,c)] for d in D)
    if score < best:
        best = score
print(best)
