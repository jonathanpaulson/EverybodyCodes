#!/usr/bin/python3 
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
G = G.split('\n')

R = len(G)
C = len(G[0])

targets = [17, 19, 22, 24, 31]
targets = [x-1 for x in targets]

ans = 0
for x in targets:
    for sy in [0,1,2]:
        for ty in [0,1,2]:
            for power in range(100):
                distance = power*3 + (sy-ty)
                if distance == x:
                    ans += sy*power
                    print(power, sy, ty)
print(ans)
