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

for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            sr,sc = r,c

def val(r,c):
    if G[r][c] in ['S', 'E']:
        return 0
    else:
        return int(G[r][c])
def diff(x,y):
    return min(abs(x-y), abs(x+10-y), abs(x-10-y))

Q = []
heapq.heappush(Q, (0,sr,sc))

SEEN = set()
while Q:
    d,r,c = heapq.heappop(Q)
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    print(f'{r=} {c=} {d=}')
    if G[r][c]=='E':
        print(d)
        break
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        rr = r+dr
        cc = c+dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
            cost = diff(val(rr,cc), val(r,c))+1
            heapq.heappush(Q, (d+cost, rr, cc))
