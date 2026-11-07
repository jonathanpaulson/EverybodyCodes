import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
C = len(G[0])
R = len(G)
assert len(G) == R
for row in G:
    assert len(row) == C

# down-right: (r,c,1,1)
# down-left: (r,c,1,-1)
# left: (r,-c,0,-1)
# up-left: (-r,c,-1,-1)
# up-right: (-r,c,-1,1)
# right: (r,c,0,1)

ans = 0
for (flip_r, flip_c, dr, dc) in [(False,False,1,1),(False,False,1,-1),(False,True,0,-1),(True,False,-1,-1),(True,False,-1,1),(False,False,0,1)]:
    score = 0
    rs = list(range(R))
    if flip_r:
        rs = list(reversed(rs))
    cs = list(range(C))
    if flip_c:
        cs = list(reversed(cs))
    SEEN = set()
    for r in rs:
        for c in cs:
            if G[r][c]!='.' and (r,c) not in SEEN:
                print(f'{r=} {c=}')
                SEEN.add((r,c))
                score += 1
                shadow = int(G[r][c])
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
                    SEEN.add((rr,cc))
                    grc = int(G[rr][cc])
                    if grc>shadow:
                        score += 1
                        shadow = grc
    ans += score
    print(f'{flip_r=} {flip_c=} {dr=} {dc=} {score=}')
print(ans)
