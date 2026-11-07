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

AMTS = {start: {10: 1}}
Q = deque([start])
while Q:
    x = Q.popleft()
    amts = AMTS[x]
    del AMTS[x]
    for amt, cnt in amts.items():
        ENERGY[x] += amt*cnt
        if amt > 1:
            for v in E[x]:
                if v in AMTS:
                    if amt-1 in AMTS[v]:
                        AMTS[v][amt-1] += cnt
                    else:
                        AMTS[v][amt-1] = cnt
                else:
                    Q.append(v)
                    AMTS[v] = {amt-1: cnt}
print(sum(ENERGY.values()))
