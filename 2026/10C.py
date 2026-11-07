import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]

#LIMIT = 10000
LIMIT = 1000000000000

GHOST = []
DR = [-1,0,1,0]
DC = [0,1,0,-1]

R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c]=='>':
            GHOST.append((r,c,1,0))
        elif G[r][c]=='v':
            GHOST.append((r,c,2,0))
        elif G[r][c]=='<':
            GHOST.append((r,c,3,0))
        elif G[r][c]=='^':
            GHOST.append((r,c,0,0))

ans = 0
t = 0
SEEN = {}
while True:
    if len(GHOST) == 0:
        break
    SIGNATURE = tuple([(r,c,d) for (r,c,d,_hits) in GHOST])
    hits = [hits for (_r,_c,_d,hits) in GHOST]
    if SIGNATURE in SEEN:
        old_t, old_hits = SEEN[SIGNATURE]
        dt = t-old_t
        assert dt>=0, f'{dt=}'
        amt = 10**20
        for i in range(len(GHOST)):
            dhits = hits[i] - old_hits[i]
            assert dhits>=0, f'{dhits=}'
            hits_remaining = LIMIT - hits[i]
            amt_i = (hits_remaining-1) // dhits
            amt = min(amt, amt_i)
        assert amt>=0, f'{amt=}'
        t += dt*amt
        NEW_GHOST = []
        for i,(r,c,d,hits) in enumerate(GHOST):
            dhits = hits - old_hits[i]
            NEW_GHOST.append((r,c,d,hits+dhits*amt))
        GHOST = NEW_GHOST
    SEEN[SIGNATURE] = (t,hits)

    t += 1
    NEW_GHOST = []
    for r,c,d,hits in GHOST:
        rr,cc = r+DR[d],c+DC[d]
        if G[rr][cc]=='#':
            ans += 1
            NEW_GHOST.append((r,c,(d+1)%4,hits+1))
        else:
            NEW_GHOST.append((rr,cc,d,hits))
    NEW_GHOST2 = []
    BY_SPOT = {}
    for r,c,d,hits in NEW_GHOST:
        if (r,c) not in BY_SPOT:
            BY_SPOT[(r,c)] = []
        BY_SPOT[(r,c)].append((d,hits))
    for (r,c),ds in BY_SPOT.items():
        if len(ds) == 1:
            NEW_GHOST2.append((r,c,ds[0][0], ds[0][1]))
        else:
            ans += len(ds)
            for d,hits in ds:
                NEW_GHOST2.append((r,c,(d+2)%4,hits+1))
    NEW_GHOST2 = [(r,c,d,hits) for (r,c,d,hits) in NEW_GHOST2 if hits<LIMIT]
    #if len(NEW_GHOST2) < len(GHOST):
    #    print(f'{t=} {len(NEW_GHOST2)=} {NEW_GHOST2=}')
    GHOST = NEW_GHOST2
print(t)
