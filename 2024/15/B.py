#!/usr/bin/python3 
import sys
from copy import deepcopy
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

items = set()
for r in range(R):
    for c in range(C):
        if r==0 and G[r][c]=='.':
            sr,sc = r,c
        if G[r][c] not in ['#', '.', '~']:
            items.add(G[r][c])
print(items)

Q = deque([(0,sr,sc, set())])
SEEN = set()
while Q:
    d,r,c, found = Q.popleft()
    key = (r,c,frozenset(found))
    if key in SEEN:
        continue
    SEEN.add(key)
    if r==sr and c==sc and found==items:
        print(d)
        break
    for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
        rr,cc = r+dr,c+dc
        if 0<=rr<R and 0<=cc<C and G[r][c]!='#':
            new_found = deepcopy(found)
            if G[rr][cc] in items:
                new_found.add(G[rr][cc])
            Q.append((d+1, rr, cc, new_found))
