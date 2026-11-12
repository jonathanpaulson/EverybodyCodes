import sys
from collections import deque
from functools import cache

@cache
def brute(P):
    P = sorted(P)
    if len(P) == 0:
        return 0
    r,c = P[0]
    without_r = frozenset([p for p in P if p[0]!=r])
    without_c = frozenset([p for p in P if p[1]!=c])
    ans = 1+min(brute(without_r), brute(without_c))
    return ans


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
            # for (r,c) have to include either rowR or colC
            PTS = set()

            while Q:
                rr,cc = Q.popleft()
                if not (0<=rr<R and 0<=cc<C and G[rr][cc]=='#'):
                    continue
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                PTS.add((rr,cc))
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    Q.append((rr+dr,cc+dc))
            score = brute(frozenset(PTS))
            #print(r,c,height,width)
            ans += score
print(ans)
