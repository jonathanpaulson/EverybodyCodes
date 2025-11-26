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
ans = 0
for r in range(R):
    for c in range(C):
        if (r-vr)**2+(c-vc)**2<=10**2 and (r,c) != (vr,vc):
            ans += int(G[r][c])
print(ans)
