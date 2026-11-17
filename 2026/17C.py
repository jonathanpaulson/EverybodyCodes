import sys
from collections import deque

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]

R = len(G)
C = len(G[0])

total = 0
for r in range(R):
    for c in range(C):
        if G[r][c]=='#':
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]=='#':
                    pass
                else:
                    total += 1

# "right hand on the wall"
# 0=north
# 1=east
# 2=south
# 3=west
DR = [-1,0,1,0]
DC = [0,1,0,-1]
ans = 1
r,c = 0,0
d = 2
while (r,c,d) != (R-1,C-1,1):
    print(f'{r=} {c=} {d=} {ans=}')
    for dd in [(d+1)%4,d,(d+3)%4,(d+2)%4]:
        rr,cc = r+DR[dd],c+DC[dd]
        if 0<=rr<R and 0<=cc<C and G[rr][cc]=='#':
            ans += {(d+2)%4: 3, d: 1, (d+1)%4: 0, (d+3)%4: 2}[dd]
            r,c,d = rr,cc,dd
            break
print(ans,total-ans)
