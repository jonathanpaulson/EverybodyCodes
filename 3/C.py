from copy import deepcopy

#infile = 'sample.in'
#infile = 'A.in'
infile = 'C.in'
G = open(infile).read().strip().split('\n')
R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]
for row in G:
    assert C == len(row)

ans = 0
d = 0
while True:
    d += 1
    changed = False
    old = deepcopy(G)
    for r in range(R):
        for c in range(C):
            if d==1 and G[r][c] == '#':
                G[r][c] = '1'
                ans += 1
                changed = True
            else:
                if r==0 or c==0 or r==R-1 or c==C-1:
                    continue
                nbrs = []
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        nbrs.append(old[r+dr][c+dc])
                ok = all(n==str(d-1) for n in nbrs)
                if ok:
                    G[r][c] = str(d)
                    ans += 1
                    changed = True
    g_str = '\n'.join(''.join(row) for row in G)
    #print(f'{d=} {ans=}')
    #print(g_str)
    if not changed:
        break
print(ans)
