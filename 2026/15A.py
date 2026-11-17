import sys
import copy
from collections import deque

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

DEPOSITS = []
for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            sr,sc = r,c
        elif G[r][c]=='E':
            er,ec = r,c
        elif G[r][c]=='@':
            DEPOSITS.append((r,c))
print(f'{len(DEPOSITS)=}')

Q = deque([])
Q.append((0,sr,sc,-1,-1,set()))
SEEN = set()
while Q:
    d,r,c,old_dr,old_dc,found = Q.popleft()
    if not (0<=r<R and 0<=c<C):
        continue
    if G[r][c]=='#':
        continue
    if G[r][c]=='@':
        found |= {(r,c)}
    K = (r,c,old_dr,old_dc,frozenset(found))
    if K in SEEN:
        continue
    #print(f'{d=} {r=} {c=} {found=}')
    SEEN.add((K))
    if (r,c) == (er,ec) and len(found) == len(DEPOSITS):
        print(d)
        break
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if (dr,dc) == (-old_dr,-old_dc):
            continue
        rr,cc = r+dr,c+dc
        Q.append((d+1,rr,cc,dr,dc,copy.copy(found)))

#print(R,C,len(DEPOSITS))
