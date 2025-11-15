import sys
from collections import deque

D = sys.stdin.read()
lines = D.splitlines()

G = []
for line in lines:
    G.append(list(line))
R = len(G)
C = len(G[0])
print(R,C)
SHEEP = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 'D':
            sr,sc = r,c
        if G[r][c] == 'S':
            SHEEP.append((r,c))
print(sorted(SHEEP))

Q = deque([])
Q.append((0,sr,sc))
DS = [(-1,2),(1,2),(-1,-2),(1,-2),
      (-2,1),(2,1),(-2,-1),(2,-1)]
EATEN = set()
SEEN = set()
while Q:
    d,r,c = Q.popleft()
    if d>20:
        continue
    if not (0<=r<R and 0<=c<C):
        continue
    if (r,c,d) in SEEN:
        continue
    SEEN.add((r,c,d))
    if d > 0:
        for (sheep_r,sheep_c) in SHEEP:
            if ((sheep_r + d, sheep_c) == (r,c) or (sheep_r+d-1, sheep_c) == (r,c)) and G[r][c]!='#':
                EATEN.add((sheep_r,sheep_c))
    #print(d,r,c,EATEN)
    for dr,dc in DS:
        Q.append((d+1,r+dr,c+dc))
print(len(EATEN))
