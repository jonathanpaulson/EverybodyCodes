#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
from copy import deepcopy
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])
print(f'{R=} {C=}')

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c

Q = deque([])
for d in range(4):
    #heapq.heappush(Q, (-384400, sr, sc, d))
    Q.append((-384400, sr, sc, d))
    #heapq.heappush(Q, (-1000, sr, sc, d))

# find cost from every top row to every end row

best = 0
SEEN = {}
DIST = {}
while Q:
    z,r,c,dir_ = Q.popleft()
    if r<0:
        continue
    z = -z
    if z<0:
        continue
    key = (r,c,dir_)
    if key in SEEN and z<=SEEN[key]:
        #assert z<=SEEN[key], f'{key=} {SEEN[key]=} {z=}'
        continue
    SEEN[key] = z
    dist_key = (r%R, c, dir_)
    if r>R and dist_key in DIST:
        #print(f'{r=} {c=} {dir_=} {z-DIST[dist_key]=}')
        assert DIST[dist_key]-z>=6
        amt = (z-100)//6
        new_z = z - 6*amt
        new_r = r + R*amt
        Q.append((-new_z, new_r, c, dir_))
        #heapq.heappush(Q, (-new_z, new_r, c, dir_))

    if r<R:
        if dist_key not in DIST:
            DIST[dist_key] = z
        else:
            DIST[dist_key] = max(DIST[dist_key], z)
        #assert dist_key not in DIST
        #DIST[dist_key] = z

    if r>best and z==0:
        print(f'{r=}')
        best = r
    if len(SEEN) % 100000 == 0:
        print(f'{len(SEEN)=} {r=} {c=} {z=} {d=}')
    for ddir in [3, 0, 1]:
        new_dir = (dir_ + ddir)%4
        dr,dc = [(-1,0), (0, 1), (1, 0), (0, -1)][new_dir]
        real_rr = r+dr
        rr = real_rr%R
        cc = c+dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
            if G[rr][cc] in ['.', 'S', 'A', 'B', 'C']:
                new_z = z-1
            elif G[rr][cc] == '-':
                new_z = z-2
            elif G[rr][cc] == '+':
                new_z = z+1
            else:
                assert False
            #heapq.heappush(Q, (-new_z, real_rr, cc, new_dir))
            Q.append((-new_z, real_rr, cc, new_dir))
