#!/usr/bin/python3 
import sys
from copy import deepcopy
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

items = set()
for r in range(R):
    for c in range(C):
        if r==0 and G[r][c]=='.':
            G[r][c]='S'
        if G[r][c] not in ['#', '.', '~']:
            items.add(G[r][c])
print(items)

pos_by_item = {item: [] for item in items}
P = set()
for r in range(R):
    for c in range(C):
        if G[r][c] in items:
            pos_by_item[G[r][c]].append((r,c))
            P.add((r,c))
item_by_pos = {(r,c): G[r][c] for (r,c) in P}

D = {p1: {} for p1 in P}
for p in P:
    D[p][p] = 0
for (sr,sc) in P:
    Q = deque([(0,sr,sc)])
    SEEN = set()
    while Q:
        d,r,c = Q.popleft()
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        if (r,c) in P and (r,c) != (sr,sc):
            D[(sr,sc)][(r,c)] = d
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            rr,cc = r+dr,c+dc
            if 0<=rr<R and 0<=cc<C and G[r][c]!='#':
                Q.append((d+1, rr, cc))

print(len(P) * 2**len(items))
sr,sc = pos_by_item['S'][0]
Q = []
heapq.heappush(Q, (0, (sr,sc), {'S'}))
SEEN = set()
while Q:
    d, pos, found = heapq.heappop(Q)
    key = (pos,frozenset(found))
    if key in SEEN:
        continue
    SEEN.add(key)
    if len(SEEN) % 1000 == 0:
        print(len(SEEN), len(Q))
    if found == items and pos == (sr,sc):
        print(d)
        break
    for p2,dist_p2 in D[pos].items():
        #print(f'{pos=} {p2=} {dist_p2=}')
        if item_by_pos[p2] in found:
            continue
        new_found = found | {item_by_pos[p2]}
        heapq.heappush(Q, (d+dist_p2, p2, new_found))
