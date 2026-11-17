import sys
from collections import deque

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]

R = len(G)
C = len(G[0])

ans = 0
for r in range(R):
    for c in range(C):
        if G[r][c]=='#':
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]=='#':
                    pass
                else:
                    ans += 1
print(ans)


Q = deque([(0,0,0)])
SEEN = set()
while Q:
    d,r,c = Q.popleft()
    if not (0<=r<R and 0<=c<C):
        continue
    if G[r][c]!='#':
        continue
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    if (r,c) == (R-1,C-1):
        print(d)
        break
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        rr,cc = r+dr,c+dc
        Q.append((d+1,rr,cc))
