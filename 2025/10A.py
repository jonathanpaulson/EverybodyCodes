import sys
from collections import deque

D = sys.stdin.read()
lines = D.splitlines()

G = []
for line in lines:
    G.append(list(line))
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'D':
            sr,sc = r,c

Q = deque([])
Q.append((0,sr,sc))
DS = [(-1,2),(1,2),(-1,-2),(1,-2),
      (-2,1),(2,1),(-2,-1),(2,-1)]
ans = 0
SEEN = set()
while Q:
    d,r,c = Q.popleft()
    print(r,c,d)
    if d>4:
        continue
    if not (0<=r<R and 0<=c<C):
        continue
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    if G[r][c] == 'S':
        ans += 1
    for dr,dc in DS:
        Q.append((d+1,r+dr,c+dc))
print(ans)
