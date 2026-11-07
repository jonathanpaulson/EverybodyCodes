import sys
from collections import deque

D = sys.stdin.read()
E = {}
for line in D.splitlines():
    a,bs = line.split(':')
    bs = bs.split(',')
    assert a not in E
    E[a] = []
    for b in bs:
        E[a].append(b)

ANS = set()
Q = deque(['NULL'])
while Q:
    x = Q.popleft()
    if x in ANS:
        continue
    ANS.add(x)
    for y in E.get(x, []):
        Q.append(y)
print(len(ANS))
