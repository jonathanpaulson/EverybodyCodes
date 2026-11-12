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

for edge in shortcuts.splitlines():
    x,y = [int(z) for z in edge.split()]
    E[x].append(y)
    E[y].append(x)

best_score_after = calcScore(E)
assert n%8==0
dx = n//8
for x in E:
    # crystals at x+i*dx for i=0..7
    # pair (x, x+i1*dx)
    # 1 has 7 options, 2 has 5 options, 3 has 3 options, 4 has 1 option
    LEFT = list(range(8))
    V = [x+i*dx for i in range(8)]
    if V[-1]>n:
        continue
    assert len(LEFT)==8
    for i1 in range(7):
        for i2 in range(5):
            for i3 in range(3):
                print(f'{i1=} {i2=} {i3=}')
                LEFT2 = deepcopy(LEFT)
                
                assert len(LEFT2)==8
                assert 1<=i1+1<len(LEFT2)
                x0,y0 = LEFT2[0],LEFT2[i1+1]
                LEFT2.pop(i1+1)
                LEFT2.pop(0)

                assert len(LEFT2)==6
                assert 1<=i2+1<len(LEFT2)
                x1,y1 = LEFT2[0],LEFT2[i2+1]
                LEFT2.pop(i2+1)
                LEFT2.pop(0)

                assert len(LEFT2)==4
                assert 1<=i3+1<len(LEFT2)
                x2,y2 = LEFT2[0],LEFT2[i3+1]
                LEFT2.pop(i3+1)
                LEFT2.pop(0)

                assert len(LEFT2)==2
                x3,y3 = LEFT2[0],LEFT2[1]

                E2 = deepcopy(E)
                E2[V[x0]].append(V[y0])
                E2[V[x1]].append(V[y1])
                E2[V[x2]].append(V[y2])
                E2[V[x3]].append(V[y3])
                E2[V[y0]].append(V[x0])
                E2[V[y1]].append(V[x1])
                E2[V[y2]].append(V[x2])
                E2[V[y3]].append(V[x3])
                score_xy = calcScore(E2)
                if score_xy < best_score_after:
                    best_score_after = score_xy
                    print(f'{x=} {y=} {best_score_after=}')
#print(score_before)
#print(best_score_after)
print(score_before - best_score_after)

