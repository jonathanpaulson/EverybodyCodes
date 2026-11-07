import sys
from collections import deque

D = sys.stdin.read()
ENERGY = {}
E = {}
for line in D.splitlines():
    id_, energy, connections = line.split()
    id_ = int(id_.removeprefix('id=').removesuffix(','))
    energy = int(energy.removeprefix('energy=').removesuffix(','))
    connections = [int(x) for x in connections.removeprefix('connections=').split(',')]
    ENERGY[id_] = energy
    E[id_] = connections

start = None
for v in E:
    if start is None or len(E[v]) > len(E[start]):
        start = v

Q = deque([(start,5)])
while Q:
    x,amt = Q.popleft()
    ENERGY[x] += amt
    if amt > 1:
        for v in E[x]:
            Q.append((v,amt-1))
print(sum(ENERGY.values()))

