import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
C = len(G[0])
R = len(G)
assert len(G) == R
for row in G:
    assert len(row) == C

SEEN = set()
ans = 0
for c in range(C):
    for r in range(R):
        #print(f'{r=} {c=} {C=} {R=} {len(G[r])=}')
        if G[r][c]!='.' and (r,c) not in SEEN:
            SEEN.add((r,c))
            ans += 1
            shadow = int(G[r][c])
            rr = r
            cc = c
            while True:
                shadow -= 1
                rr += 1
                cc += 1
                if rr>=R or cc>=C or G[rr][cc]=='.':
                    break
                SEEN.add((rr,cc))
                grc = int(G[rr][cc])
                if grc>shadow:
                    ans += 1
                    shadow = grc
print(ans)
