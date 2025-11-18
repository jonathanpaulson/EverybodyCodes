import sys
from collections import deque

D = sys.stdin.read()
G = [[int(x) for x in row] for row in D.splitlines()]
R = len(G)
C = len(G[0])

DS = [(-1,0),(1,0),(0,-1),(0,1)]
Q = deque([])
Q.append((0,0))
Q.append((R-1,C-1))
SEEN = set()
while Q:
    r,c = Q.popleft()
    if 0<=r<R and 0<=c<C:
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        for dr,dc in DS:
            rr,cc = r+dr,c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]:
                Q.append((rr,cc))
print(len(SEEN))
