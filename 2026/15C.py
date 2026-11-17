import sys
import copy
import heapq
from collections import deque

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

# each branching path must be followed in full. just count which has the best stone/time ratio?
# we can also go around a full circle!

DEPOSITS = []
for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            sr,sc = r,c
        elif G[r][c]=='E':
            er,ec = r,c
        elif G[r][c]=='@':
            DEPOSITS.append((r,c))

OPTS = []
assert sr==er
for c1 in range(C):
    assert G[sr][c] in '.SE', f'{c=} {G[sr][c]=}'
    up_score = None
    for r1 in [sr-1,sr+1]:
        if G[r1][c1] in '.@':
            Q = deque([])
            Q.append((1,r1,c1,-1 if r1==sr-1 else 1,0,0))
            while Q:
                d,r,c,old_dr,old_dc,found = Q.popleft()
                if not (0<=r<R and 0<=c<C):
                    continue
                if G[r][c]=='#':
                    continue
                if G[r][c]=='@':
                    found += 1
                if r==sr and c!=c1:
                    total_time = d+abs(c-c1)
                    print(f'{c1=} {r1=} {r=} {c=} {total_time=} {found=}')
                    OPTS.append((total_time, found))
                    if r1==sr-1:
                        up_score = (total_time, found)
                    elif up_score is not None:
                        up_total_time, up_found = up_score
                        around_total_time = total_time + up_total_time - 2*abs(c-c1)
                        around_found = found + up_found
                        OPTS.append((around_total_time, around_found))
                        print(f'AROUND {r1=} {c1=} {around_total_time=} {around_found=}')
                    continue
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if (dr,dc) == (-old_dr,-old_dc):
                        continue
                    rr,cc = r+dr,c+dc
                    Q.append((d+1,rr,cc,dr,dc,found))

OPTS = sorted(OPTS, key=lambda kv:kv[1]/kv[0])
print(OPTS)
best_total_time, best_found = OPTS[-1]

TARGET = 202620262026
best_amt = (TARGET-200)//best_found
start_time = best_amt * best_total_time
TARGET -= best_amt * best_found

Q = []
Q.append((0,sr,sc,-1,-1,0))
highest_d = 0
SEEN = {}
SEEN2 = set()

while Q:
    d,r,c,old_dr,old_dc,found = heapq.heappop(Q)
    if d > highest_d:
        #print(f'{d=} {found=}')
        highest_d = d
    if not (0<=r<R and 0<=c<C):
        continue
    if G[r][c]=='#':
        continue
    if G[r][c]=='@':
        found += 1

    K2 = (r,c,old_dr,old_dc,found)
    if K2 in SEEN2:
        continue
    SEEN2.add(K2)
    if found>TARGET:
        continue

    #K = (r,c,old_dr,old_dc)
    #if K in SEEN and d<500:
    #    old_d, old_found = SEEN[K]
    #    dd = d-old_d
    #    dfound = found - old_found
    #    if dfound > 0 and dd>0:
    #        amt = (TARGET-15-found)//dfound
    #        print(f'{amt=} {len(SEEN)=} {dd=} {dfound=} {(r,c)=} {(old_dr,old_dc)=}')
    #        heapq.heappush(Q, (d+amt*dd,r,c,old_dr,old_dc,found+amt*dfound))
    #    continue
    #SEEN[K] = d,found


    #print(f'{d=} {r=} {c=} {found=}')
    if (r,c) == (er,ec) and found==TARGET:
        print(d+start_time)
        break
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if (dr,dc) == (-old_dr,-old_dc):
            continue
        rr,cc = r+dr,c+dc
        heapq.heappush(Q, (d+1,rr,cc,dr,dc,found))

#print(R,C,len(DEPOSITS))
