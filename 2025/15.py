import sys
import heapq
from collections import deque
from copy import deepcopy

r = 0
c = 0
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
d = 0

WALL = set()
I = [(0,0)]
D = sys.stdin.read()
for i,instr in enumerate(D.split(',')):
    turn = instr[0]
    amt = int(instr[1:])
    if turn == 'R':
        d = (d+1)%4
    else:
        d = (d+3)%4
    r += amt*DIRS[d][0]
    c += amt*DIRS[d][1]
    I.append((r,c))

Rs = []
Cs = []
for (r,c) in I:
    Rs.append(r-1)
    Rs.append(r)
    Rs.append(r+1)
    Cs.append(c-1)
    Cs.append(c)
    Cs.append(c+1)
Rs = sorted(set(Rs))
Cs = sorted(set(Cs))

Rsmall = {r: i for i,r in enumerate(Rs)}
Csmall = {c: i for i,c in enumerate(Cs)}

Rbig = {i: r for i,r in enumerate(Rs)}
Cbig = {i: c for i,c in enumerate(Cs)}

r = 0
c = 0
d = 0
WALL = set()
for i,instr in enumerate(D.split(',')):
    turn = instr[0]
    amt = int(instr[1:])
    if turn == 'R':
        d = (d+1)%4
    else:
        d = (d+3)%4
    old_r = Rsmall[r]
    old_c = Csmall[c]
    r += amt*DIRS[d][0]
    c += amt*DIRS[d][1]
    new_r = Rsmall[r]
    new_c = Csmall[c]
    for rr in range(min(old_r,new_r), max(old_r,new_r)+1):
        for cc in range(min(old_c,new_c),max(old_c,new_c)+1):
            WALL.add((rr,cc))

er,ec = r,c
WALL.discard((Rsmall[0],Csmall[0]))
WALL.discard((Rsmall[er],Csmall[ec]))

if True:
    WR = max([r for (r,c) in WALL])
    WC = max([c for (r,c) in WALL])
    for r in range(0,WR+2):
        row = []
        for c in range(0,WC+2):
            ch = '#' if (r,c) in WALL else '.'
            if (r,c)==(Rsmall[0],Csmall[0]):
                ch = 'S'
            if (r,c) == (Rsmall[er],Csmall[ec]):
                ch = 'E'
            row.append(ch)
        print(''.join(row))


Q = []
def add_queue(d,r,c):
    heapq.heappush(Q, (d, r, c))
#assert False, f'{er=} {ec=}'

add_queue(0,Rsmall[0],Csmall[0])
SEEN = set()
while Q:
    d,r,c = heapq.heappop(Q)
    assert d>=0
    if (r,c) == (Rsmall[er],Csmall[ec]):
        print(d)
        sys.exit(0)
    if (r,c) in WALL:
        continue
    if (r,c) in SEEN:
        continue
    #print(f'{r=} {c=} {d=} {Rsmall[er]=} {Csmall[ec]=} {Ramt[r]=} {Camt[c]=} {(er,ec)=} {d+Ramt[r]*Camt[c]=}')
    SEEN.add((r,c))
    #if len(SEEN)%100000==0:
    #    print(f'{_dist_end=} {r=} {c=} {d=} {(er,ec)=}')
    for dr,dc in DIRS:
        new_r = r+dr
        new_c = c+dc
        new_dist = d+abs(Rbig[new_r]-Rbig[r]) + abs(Cbig[new_c]-Cbig[c])
        add_queue(new_dist, new_r, new_c)
