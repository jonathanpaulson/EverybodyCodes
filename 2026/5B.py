import sys
from collections import deque

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])
assert R%2==1 and C%2==1

ONES = set()
for r in range(R):
    for c in range(C):
        if G[r][c]=='1':
            ONES.add((r,c))

Q = deque([(R//2,C//2)])
LAND = set()
while Q:
    r,c = Q.popleft()
    #print(f'{r=} {c=}')
    if (r,c) in LAND:
        continue
    LAND.add((r,c))
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr,cc = r+dr,c+dc
            if (rr,cc) == (r,c):
                continue
            N = [(rr+dr2,cc+dc2) for dr2 in [-1,0,1] for dc2 in [-1,0,1]]
            good_n = 0
            for (nr,nc) in N:
                if (nr,nc) != (rr,cc) and ((nr,nc) in LAND or (nr,nc) in ONES):
                    good_n += 1
            #print(f'{rr=} {cc=} {good_n=}')
            if good_n >= 5:
                Q.append((rr,cc))

SAND = set()
for (r,c) in LAND:
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr,cc = r+dr,c+dc
            if not (0<=rr<R and 0<=cc<C):
                print(f'EDGE {r=} {c=}')
                SAND.add((r,c))
            elif (rr,cc) not in LAND:
                print(f'WATER {r=} {c=}')
                SAND.add((r,c))
while True:
    changed = False
    for (r,c) in LAND:
        if (r,c) in SAND:
            continue
        nsand = 0
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if (r+dr,c+dc) in SAND:
                    nsand += 1
        if nsand >= 5:
            print(f'{r=} {c=} {nsand=}')
            SAND.add((r,c))
            changed = True
    if not changed:
        break

print(len(LAND))
print(len(SAND))
