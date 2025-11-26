import sys
import heapq
from collections import deque
from copy import deepcopy

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c]=='@':
            vr,vc = r,c
        elif G[r][c]=='S':
            sr,sc = r,c
        else:
            G[r][c] = int(G[r][c])
G[sr][sc] = 0

def bfs(start, rad, go_left):
    D = {}
    Q = []
    heapq.heappush(Q, (0, start[0], start[1]))
    while Q:
        d,r,c = heapq.heappop(Q)
        if not (0<=r<R and 0<=c<C):
            continue
        if (r-vr)**2+(c-vc)**2<=rad**2:
            continue
        if r==vr and ((go_left and c>vc) or ((not go_left) and c<vc)):
            continue
        if (r,c) in D:
            continue
        D[(r,c)] = d
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            heapq.heappush(Q, (d+G[r][c], r+dr, c+dc))
    return D


# need to start at S, make a loop, and return to S
# need to pass through (vr,<vc) and (vr,>vc) and (>vr,vc)
for rad in range(1000):
    time_limit = (rad+1)*30-1
    Dleft = bfs((sr,sc), rad, True)
    Dright = bfs((sr,sc), rad, False)

    score = 10**9
    for r in range(vr+1,R):
        if (r,vc) in Dleft:
            score = min(score, Dleft[(r, vc)]+Dright[(r, vc)]+int(G[r][vc]))
    if score < time_limit:
        print(rad, score)
        print(rad*score)
        assert False
