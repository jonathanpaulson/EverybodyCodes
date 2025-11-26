import sys
import heapq
from collections import deque
from copy import deepcopy

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c]=='@':
            vr,vc = r,c
best = None
for rad in range(1,1000):
    score = 0
    for r in range(R):
        for c in range(C):
            if (rad-1)**2<(r-vr)**2+(c-vc)**2<=rad**2 and (r,c) != (vr,vc):
                score += int(G[r][c])
    if best is None or score > best[0]:
        best = (score, score*rad)
print(best[1])
