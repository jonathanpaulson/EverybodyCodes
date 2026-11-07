import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
C = len(G[0])
R = len(G)
for r in range(R):
    for c in range(C):
        if G[r][c]!='.':
            G[r][c] = int(G[r][c])
assert len(G) == R
for row in G:
    assert len(row) == C

# down-right: (r,c,1,1)
# down-left: (r,c,1,-1)
# left: (r,-c,0,-1)
# up-left: (-r,c,-1,-1)
# up-right: (-r,c,-1,1)
# right: (r,c,0,1)
DIRECTIONS = [
    ('SE', False,False,1,1),
    ('SW', False,False,1,-1),
    ('W', False,True,0,-1),
    ('NW', True,False,-1,-1),
    ('NE', True,False,-1,1),
    ('E',False,False,0,1)
]

t = 0
warriors = 0
SEEDS = {}
ans = 0
while True:
    dir_name, flip_r, flip_c, dr, dc = DIRECTIONS[t%6]
    t += 1

    for (r,c),d in SEEDS.items():
        if d==0:
            G[r][c]=1
        SEEDS[(r,c)] = d-1
    SEEDS = {k:v for k,v in SEEDS.items() if v>=0}

    old_warriors = warriors
    old_ans = ans
    #for r in range(R):
    #    for c in range(C):
    #        print(G[r][c],end='')
    #    print()

    rs = list(range(R))
    if flip_r:
        rs = list(reversed(rs))
    cs = list(range(C))
    if flip_c:
        cs = list(reversed(cs))
    SEEN = set()
    for r in rs:
        for c in cs:
            if G[r][c]!='.' and G[r][c]!='X' and (r,c) not in SEEN:
                SEEN.add((r,c))
                shadow = G[r][c]
                ans += 1
                if G[r][c]==9:
                    warriors += 1
                    G[r][c]='X'
                    SEEDS[(r,c)] = 3
                else:
                    G[r][c] += 1
                rr = r
                cc = c
                while True:
                    rr += dr
                    cc += dc
                    if not (0<=rr<R and 0<=cc<C):
                        break
                    if G[rr][cc]=='.':
                        continue
                    shadow -= 1
                    if G[rr][cc]=='X':
                        continue
                    SEEN.add((rr,cc))
                    grc = G[rr][cc]
                    if grc>shadow:
                        ans += 1
                        shadow = grc
                        if G[rr][cc]==9:
                            warriors += 1
                            G[rr][cc]='X'
                            SEEDS[(rr,cc)] = 3
                        else:
                            G[rr][cc] += 1
    #print(f'{t:3} {dir_name:2} {ans-old_ans:4} {warriors-old_warriors:4} {warriors:4} {ans:4}')
    if warriors >= 100000:
        break
    #print(f'{flip_r=} {flip_c=} {dr=} {dc=} {score=}')
print(ans)
