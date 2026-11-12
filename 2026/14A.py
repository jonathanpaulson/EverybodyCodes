import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])
ans = 0
for r in range(R):
    for c in range(C):
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            rr,cc = r+dr,c+dc
            if not (0<=rr<R and 0<=cc<C):
                ans += 1
                continue
            if G[rr][cc] != G[r][c]:
                ans += 0.5
print(ans)

