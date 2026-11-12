import sys
from collections import deque
from copy import deepcopy

def calcScore(E):
    ans = 0
    for x in E:
        x_ans = 0
        Q = deque([(x,0)])
        SEEN = set()
        while Q:
            y,d = Q.popleft()
            if y in SEEN:
                continue
            SEEN.add(y)
            x_ans += d
            #print(f'{x=} {y=} {d=}')
            for z in E[y]:
                Q.append((z, d+1))
        ans += x_ans
        #assert len(SEEN) == len(E)
        #print(f'{x=} {x_ans=}')
    return ans


D = sys.stdin.read()
portals, shortcuts = D.split('\n\n')
n = int(portals.removeprefix('portals: '))
E = {x+1: [] for x in range(n)}
for x in range(n):
    for dx in [-3,-2,-1,1,2,3]:
        y = (x+1+dx)
        if y<1:
            y += n
        if y>n:
            y -= n
        E[x+1].append(y)
score_before = calcScore(E)

#assert False

for edge in shortcuts.splitlines():
    x,y = [int(z) for z in edge.split()]
    E[x].append(y)
    E[y].append(x)
best_score_after = calcScore(E)
for x in E:
    for y in E:
        E2 = deepcopy(E)
        E2[x].append(y)
        E2[y].append(x)
        score_xy = calcScore(E2)
        if score_xy < best_score_after:
            best_score_after = score_xy
            print(f'{x=} {y=} {best_score_after=}')
print(score_before)
print(best_score_after)
print(score_before - best_score_after)

