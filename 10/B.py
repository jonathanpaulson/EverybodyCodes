import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G_BIG = open(infile).read().strip()
G_BIG = G_BIG.split('\n')

R = 8
C = 8

ans = 0
count = 0
for br in range(0, len(G_BIG), 9):
    for bc in range(0, len(G_BIG[br]), 9):
        count += 1
        G = [[G_BIG[br+j][bc+i] for i in range(C)] for j in range(R)]
        #print([''.join(row) for row in G])
        i = 0
        for r in range(R):
            for c in range(C):
                if G[r][c] == '.':
                    row = {G[r][cc] for cc in range(C)}
                    col = {G[rr][c] for rr in range(R)}
                    final = row & col
                    final.discard('.')
                    assert len(final) == 1
                    #G[r][c] = list(final)[0]
                    ch = list(final)[0]
                    ch_int = ord(ch)-ord('A')+1
                    i += 1
                    #print(i, ch, ch_int)
                    ans += i * ch_int
#print(count)
print(ans)
