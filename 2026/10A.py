import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]

GHOST = []
DR = [-1,0,1,0]
DC = [0,1,0,-1]

R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c]=='>':
            GHOST.append((r,c,1))
        elif G[r][c]=='v':
            GHOST.append((r,c,2))
        elif G[r][c]=='<':
            GHOST.append((r,c,3))
        elif G[r][c]=='^':
            GHOST.append((r,c,0))

ans = 0
for _ in range(10):
    NEW_GHOST = []
    for r,c,d in GHOST:
        rr,cc = r+DR[d],c+DC[d]
        if G[rr][cc]=='#':
            ans += 1
            NEW_GHOST.append((r,c,(d+1)%4))
        else:
            NEW_GHOST.append((rr,cc,d))
    NEW_GHOST2 = []
    BY_SPOT = {}
    for r,c,d in NEW_GHOST:
        if (r,c) not in BY_SPOT:
            BY_SPOT[(r,c)] = []
        BY_SPOT[(r,c)].append(d)
    for (r,c),ds in BY_SPOT.items():
        if len(ds) == 1:
            NEW_GHOST2.append((r,c,ds[0]))
        else:
            ans += len(ds)
            for d in ds:
                NEW_GHOST2.append((r,c,(d+2)%4))
    GHOST = NEW_GHOST2
print(ans)




