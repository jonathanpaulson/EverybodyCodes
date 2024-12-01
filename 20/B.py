#!/usr/bin/python3 
import sys
from collections import defaultdict, deque
from copy import deepcopy
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'B.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c
        if G[r][c] == 'A':
            ar,ac = r,c
        if G[r][c] == 'B':
            br,bc = r,c
        if G[r][c] == 'C':
            cr,c_c = r,c

#cost = 10**9
#for r in range(R):
#    for c in range(C):
#        for dir_ in range(4):
#            if G[r][c]!='#':
#                cost_rcd = getCost(r,c,dir_)
#                print(f'{r=} {c=} {cost_rcd=}')
#                if cost_rcd < cost:
#                    cost = cost_rcd
#                    print(f'{r=} {c=} {dir_=} {cost_rcd=}')

Q = []
for d in range(4):
    heapq.heappush(Q, (0,0, 0, sr, sc, 10000, d))

SEEN = set()
BEST = {}
cost = 10**9
best = 10**9
while Q:
    est, d, target, r, c, z, dir_ = heapq.heappop(Q)
    if z<9900 or z>10100:
        continue
    # A B C S
    #if target == 3 and z>=10000 and G[r][c]=='S':
    if target == 3 and G[r][c]=='S' and z>=10000:
        score = d + max(0, 10000-z)
        if score < best:
            print(f'BEST {score=} {d=} {z=}')
            best = score
            break
    key = (target,r,c,z,dir_)
    if key in SEEN:
        continue
    SEEN.add(key)
    if len(SEEN) % 100000 == 0:
        print(f'{len(SEEN)=} {target=} {r=} {c=} {z=} {d=} {est=}')
    #best_key = (target, r, c, dir_)
    #if best_key in BEST and BEST[best_key] < z:
    #    continue
    #BEST[best_key] = z
    for ddir in [3, 0, 1]:
        new_dir = (dir_ + ddir)%4
        dr,dc = [(-1,0), (0, 1), (1, 0), (0, -1)][new_dir]
        rr = r+dr
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
            if target==0 and G[rr][cc]=='A':
                new_target = 1
            elif target==1 and G[rr][cc]=='B':
                new_target = 2
            elif target==2 and G[rr][cc]=='C':
                new_target = 3
            else:
                new_target = target
            target_r, target_c = [(ar, ac), (br, bc), (cr, c_c), (sr,sc)][new_target]
            est = d+1+abs(target_r-r)+abs(target_c-c)#+max(0, 10000-z)
            if new_target==0:
                est += abs(br-ar)+abs(bc-ac)+abs(cr-br)+abs(c_c-bc)+abs(sr-cr)+abs(sc-c_c)
            elif new_target==1:
                est += abs(cr-br)+abs(c_c-bc)+abs(sr-cr)+abs(sc-c_c)
            elif new_target==2:
                est += abs(sr-cr)+abs(sc-c_c)
            else:
                est += 0
            if est<d+1+max(0,10000-z):
                est = d+1+max(0,10000-z)
            #print(f'{target_r=} {target_c=}')
            #est = d+1
            if d+1<=564:
                heapq.heappush(Q, (est, d+1, new_target, rr, cc, new_z, new_dir))
