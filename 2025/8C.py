import sys

D = sys.stdin.read()

xs = [int(x) for x in D.split(',')]
print(xs, len(xs))

N = 256

E = []
for i in range(len(xs)-1):
    x,y = xs[i], xs[i+1]
    E.append((x,y))

ans = 0
for x1 in range(1,256+1):
    for y1 in range(1,256+1):
        score = 0
        for i2,e2 in enumerate(E):
            x2,y2 = e2
            ok = True
            if x2 in [x1,y1] or y2 in [x1,y1]:
                ok = False
            m1,m2 = min(x1,y1),max(x1,y1)
            if (((m1<=x2<=m2) != (m1<=y2<=m2)) and ok) or (x2,y2)==(x1,y1):
                score += 1
        ans = max(ans, score)
            #print(f'{i1=} {i2=} {e1=} {e2=} {ans=}')
print(ans)
