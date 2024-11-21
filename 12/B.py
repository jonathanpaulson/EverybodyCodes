#!/usr/bin/python3 
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()
G = G.split('\n')

R = len(G)
C = len(G[0])

targets = []
sources = []
for y in range(R):
    for x in range(C):
        if G[y][x]=='T':
            targets.append((x,R-y))
        elif G[y][x]=='H':
            targets.append((x,R-y))
            targets.append((x,R-y))
        elif G[y][x] in ['A', 'B', 'C']:
            sources.append((x,R-y))

ans = 0
for (tx,ty) in targets:
    found = False
    for (sx,sy) in sources:
        for power in range(100):
            distance = power*3 + (sy-ty)
            if sy+power >= ty and sx+distance==tx:
                assert not found
                found = True
                ans += (sy-1)*power
                print(f'{sx=} {sy=} {tx=} {ty=} {power=}')
    assert found
print(ans)
