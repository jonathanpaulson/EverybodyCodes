#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

P = []
for r in range(R):
    for c in range(C):
        if G[r][c] == '*':
            P.append((r,c))

E = []
UF = {p: p for p in P}
for p1 in P:
    for p2 in P:
        if p1 != p2:
            distance = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
            E.append((distance, p1, p2))

def find(x):
    if UF[x] == x:
        return x
    UF[x] = find(UF[x])
    return UF[x]
def mix(p1,p2):
    UF[find(p1)] = find(p2)

E = sorted(E)
ans = 0
for (cost, p1, p2) in E:
    if find(p1) != find(p2):
        print(cost,p1,p2)
        ans += cost
        mix(p1,p2)
ans += len(P)

print(ans)
