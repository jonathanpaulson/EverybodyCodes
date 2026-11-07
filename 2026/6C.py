import sys
from collections import deque, defaultdict

D = sys.stdin.read()
E = defaultdict(list)
V = set()
for line in D.splitlines():
    a,bs = line.split(':')
    bs = bs.split(',')
    V.add(a)
    #assert a not in E
    #E[a] = []
    for b in bs:
        V.add(b)
        E[b].append(a)

ANSS = []
for x in V:
    if 'NULL' in x:
        ANS = set()
        Q = deque([x])
        while Q:
            x = Q.popleft()
            if x in ANS:
                continue
            ANS.add(x)
            for y in E.get(x, []):
                Q.append(y)
        ANSS.append(ANS)

FINAL = set()
for i in range(len(ANSS)):
    for j in range(i+1, len(ANSS)):
        FINAL |= ANSS[i] & ANSS[j]
print(len(FINAL))
