#infile = 'sample.in'
infile = 'A.in'
G = open(infile).read().strip().split('\n')
G = [[int(x) for x in row.split()] for row in G]
R = len(G)
C = len(G[0])
G = [[G[r][c] for r in range(R)] for c in range(C)]
R,C = C,R
assert R == 4

for t in range(10):
    # move G[t%R][0] to somewhere in the next column
    to_ = G[(t+1)%R]
    move = G[t%R][0]
    G[t%R] = [G[t%R][i] for i in range(0)] + [G[t%R][i] for i in range(0+1, len(G[t%R]))]
    pos = (move-1) % (2*len(to_))
    #print(f'{move=} {pos=} {to_=}')
    if pos<len(to_):
        G[(t+1)%R] = [to_[i] for i in range(pos)] + [move] + [to_[i] for i in range(pos, len(to_))]
    else:
        pos = 2*len(to_) - pos
        G[(t+1)%R] = [to_[i] for i in range(pos)] + [move] + [to_[i] for i in range(pos, len(to_))]
    #print(f'{pos=} {G[(t+1)%R]=}')
    #print(f'{G=}')
    score = 0
    for r in range(R):
        score = score*10 + G[r][0]
    print(t+1, score)
