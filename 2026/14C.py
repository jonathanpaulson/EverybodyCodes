import sys

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])
ans = 0
V = set()
for r in range(R):
    for c in range(C):
        V.add(G[r][c])
V.add('')

E = {v: {v: 0 for v in V} for v in V}
for r in range(R):
    for c in range(C):
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            rr,cc = r+dr,c+dc
            if not (0<=rr<R and 0<=cc<C):
                E[''][G[r][c]] += 2
                E[G[r][c]][''] += 2
                continue
            if G[rr][cc] != G[r][c]:
                E[G[r][c]][G[rr][cc]] += 1
                E[G[rr][cc]][G[r][c]] += 1

best = 10**10
for free1 in V:
    for free2 in V:
        if free1 == '' or free2 == '':
            continue
        edges = []
        for a in V:
            for b in V:
                if E[a][b]>0:
                    #print(f'{a=} {b=} {E[a][b]=}')
                    cost = E[a][b]
                    if len({a,b} & {free1,free2})>0:
                        cost = 0
                    edges.append((cost, a,b))

        UF = {v: v for v in V}
        def find(x):
            if UF[x] == x:
                return x
            UF[x] = find(UF[x])
            return UF[x]
        def mix(a,b):
            UF[find(a)] = find(b)

        edges = sorted(edges)
        ans = 0
        for cost,a,b in edges:
            if find(a) != find(b):
                #print(f'{a=} {b=} {cost=}')
                mix(a,b)
                ans += cost
        ans //= 2
        if ans < best:
            print(f'{free1=} {free2=} {ans=}')
            best = ans
print(best)
