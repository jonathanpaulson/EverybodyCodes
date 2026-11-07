import sys

def f(a,b):
    score = 0
    for i in range(len(b)):
        ai = int(a[i%len(a)])
        xi = int(b[i])*ai**i
        score += xi
    return score

D = sys.stdin.read()
ans = 0
for line in D.splitlines():
    a,b = line.split()
    a = a.removeprefix('ISO2-')
    bval = int(b)
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    score = f(a,b)
    ok = True
    for c in range(bval):
        if f(a,''.join(reversed(str(c)))) == score:
            ok = False
    print(f'{a=} {b=} {score=} {ok=}')
    if ok:
        ans += score
print(ans)
