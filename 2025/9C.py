import sys
from collections import defaultdict

D = sys.stdin.read()
lines = D.splitlines()
PEOPLE = {}
for line in lines:
    k,v = line.split(':')
    PEOPLE[k] = v

UF = {k: k for k in PEOPLE}
def find(x):
    if x==UF[x]:
        return x
    else:
        UF[x] = find(UF[x])
        return UF[x]
def merge(x, y):
    UF[find(x)] = find(y)

ans = 0
for k, v in PEOPLE.items():
    for p1k, p1v in PEOPLE.items():
        for p2k, p2v in PEOPLE.items():
            if len({k,p1k,p2k}) == 3:
                is_ok = True
                for i in range(len(v)):
                    if v[i] != p1v[i] and v[i]!=p2v[i]:
                        is_ok = False
                        break
                if is_ok:
                    print(f'{k=} {p1k=} {p2k=}')
                    merge(k, p1k)
                    merge(k, p2k)

SZ = defaultdict(int)
for k in PEOPLE:
    SZ[find(k)] += 1
best = None
for k,sz in SZ.items():
    if best is None or sz>SZ[best]:
        best = k

ans = 0
for k in PEOPLE:
    if find(k) == best:
        ans += int(k)
print(ans)
