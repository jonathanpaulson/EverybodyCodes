import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

ans = ''
for r in range(R):
    for c in range(C):
        if G[r][c] == '.':
            row = {G[r][cc] for cc in range(C)}
            col = {G[rr][c] for rr in range(R)}
            final = row & col
            final.discard('.')
            assert len(final) == 1
            #G[r][c] = list(final)[0]
            ans = ans + list(final)[0]
print(G)
print(ans)
