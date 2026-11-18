import sys
import heapq

D = sys.stdin.read()

ON = set()
x0 = None
x1 = None
y0 = None
y1 = None

X = []
H = {}

for line in D.splitlines():
    x,y,width = line.split()
    x = int(x.removeprefix('x='))
    y = int(y.removeprefix('y='))
    width = int(width.removeprefix('width='))
    assert width>=1
    H[x] = y
    X.append(x)
    if width>1:
        H[x+width-1] = y
        X.append(x+width-1)

left_h = 0
right_h = max(H.values())
X = sorted(X)
ans = 0
for x0,x1 in zip(X,X[1:]):
    assert x0 in H
    assert x1 in H
    left_h = max(left_h, H[x0])
    right_h = max([H[xx] for xx in H.keys() if xx>=x1])
    mid_h = min(left_h, right_h)
    ans += max(H[x0], mid_h)
    if x1>x0:
        ans += (x1-x0-1)*mid_h
    print(f'After [{x0},{x1}): {(left_h, mid_h, right_h)=} {H[x0]=} {ans=}')
    #right_h = max([H[xx] for xx in H.keys() if xx>=x1
ans += H[X[-1]]
print(ans)
