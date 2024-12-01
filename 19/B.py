#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
from copy import deepcopy
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()

msg, G = G.split('\n\n')
G = G.split('\n')
R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

for t in range(100):
    mi = 0
    print(f'{t=}')
    for r in range(R):
        for c in range(C):
            if r>0 and r<R-1 and c>0 and c<C-1:
                ch = msg[mi]
                mi = (mi+1)%len(msg)

                M = {(-1,-1): (-1,0),
                     (-1,0): (-1,1),
                     (-1, 1): (0, 1),
                     (0, 1): (1, 1),
                     (1, 1): (1, 0),
                     (1, 0): (1, -1),
                     (1, -1): (0, -1),
                     (0, -1): (-1, -1)}
                OLD = {(dr,dc): G[r+dr][c+dc] for dr,dc in M.keys()}
                if ch=='L':
                    for (fr,fc),(sr,sc) in M.items():
                        G[r+fr][c+fc] = OLD[(sr,sc)]
                elif ch=='R':
                    for (sr,sc),(fr,fc) in M.items():
                        #print(f'{r+fr=} {c+fc=} {r+sr=} {
                        G[r+fr][c+fc] = OLD[(sr,sc)]
                #print('\n'.join(''.join(row) for row in G))
                #print(f'{r=} {c=} {ch=}')
                #if ch=='L':
                #    for (fr,fc),(sr,sc) in M.items():
                #        NG[r+fr][c+fc] = G[r+sr][c+sc]
                #elif ch=='R':
                #    for (sr,sc),(fr,fc) in M.items():
                        #print(f'{r+fr=} {c+fc=} {r+sr=} {
                #        NG[r+fr][c+fc] = G[r+sr][c+sc]
                #G = deepcopy(NG)

print('\n'.join(''.join(row) for row in G))
