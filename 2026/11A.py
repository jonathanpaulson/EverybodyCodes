import sys
from collections import deque

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
            print(f'{x=} {y=} {d=}')
            for z in E[y]:
                Q.append((z, d+1))
        ans += x_ans
        #assert len(SEEN) == len(E)
        print(f'{x=} {x_ans=}')
    return ans


D = sys.stdin.read()
portals, shortcuts = D.split('\n\n')
n = int(portals.removeprefix('portals: '))
E = {x+1: [] for x in range(n)}
for x in range(n):
    E[x+1].append(x if x>=1 else n)
    E[x+1].append(x+2 if x+2<=n else 1)
score_before = calcScore(E)
print(E)

#assert False

for edge in shortcuts.splitlines():
    x,y = [int(z) for z in edge.split()]
    E[x].append(y)
    E[y].append(x)
score_after = calcScore(E)
print(score_before - score_after)

