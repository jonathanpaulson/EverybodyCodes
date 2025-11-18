import sys
from collections import deque
from copy import deepcopy

D = sys.stdin.read()
G = [[int(x) for x in row] for row in D.splitlines()]
R = len(G)
C = len(G[0])

DS = [(-1,0),(1,0),(0,-1),(0,1)]

def score(sr,sc,SEEN):
    NEW_SEEN = deepcopy(SEEN)
    Q = deque([])
    Q.append((sr,sc))
    while Q:
        r,c = Q.popleft()
        if 0<=r<R and 0<=c<C:
            if (r,c) in NEW_SEEN:
                continue
            NEW_SEEN.add((r,c))
            for dr,dc in DS:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]:
                    Q.append((rr,cc))
    return NEW_SEEN

print(R,C)
SEEN = set()
for t in range(3):
    best = None
    for r1 in range(R):
        for c1 in range(C):
            SEEN_r1c1 = score(r1,c1,SEEN)
            if best is None or len(SEEN_r1c1)>len(best[0]):
                best = (SEEN_r1c1, (r1,c1))
    SEEN |= best[0]
    print(t, best[1], len(SEEN))
print(len(SEEN))
