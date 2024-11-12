import sys
infile = sys.argv[1] if len(sys.argv)>=2 else '1_3.in'
D = open(infile).read().strip()
ans = 0
i = 0
while i < len(D):
    c1 = D[i]
    c2 = D[i+1]
    c3 = D[i+2]
    i += 3
    n_enemies = 0
    for c in [c1,c2,c3]:
        ans += {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}[c]
        if c != 'x':
            n_enemies += 1
    if n_enemies == 2:
        ans += 2
    if n_enemies == 3:
        ans += 6
print(ans)
