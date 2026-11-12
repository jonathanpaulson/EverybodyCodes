import sys
from collections import deque


D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

ans = 0

SEEN = set()
for r in range(R):
    for c in range(C):
        if G[r][c]=='#':
            if (r,c) in SEEN:
                continue
            Q = deque([(r,c)])
            r0 = r
            r1 = r
            c0 = c
            c1 = c
            while Q:
                rr,cc = Q.popleft()
                if not (0<=rr<R and 0<=cc<C and G[rr][cc]=='#'):
                    continue
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                r0 = min(r0,rr)
                r1 = max(r1,rr)
                c0 = min(c0,cc)
                c1 = max(c1,cc)
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    Q.append((rr+dr,cc+dc))
            height = r1-r0+1
            width = c1-c0+1
            print(r,c,height,width)
            ans += min(height,width)
print(ans)
