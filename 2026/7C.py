import sys
from copy import deepcopy
from collections import deque

LIMIT = 1000000
#LIMIT = 100
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

def total_energy(ENERGY, E, start):
    AMTS = {start: {10: 1}}
    Q = deque([start])

    DEAD = set()
    stage = 0
    while True:
        stage += 1
        #print(f'Stage {stage}:')
        #for k,v in sorted(AMTS.items()):
        #    if k not in DEAD:
        #        print(f'Cloud {k} received {v}')
        #print()
        NEW_AMTS = {}
        for x,amts in AMTS.items():
            if x in DEAD:
                continue
            for amt, cnt in amts.items():
                ENERGY[x] += amt*cnt
                if amt > 1:
                    for v in E[x]:
                        if v in NEW_AMTS:
                            if amt-1 in NEW_AMTS[v]:
                                NEW_AMTS[v][amt-1] += cnt
                            else:
                                NEW_AMTS[v][amt-1] = cnt
                        else:
                            NEW_AMTS[v] = {amt-1: cnt}
        for v, v_energy in ENERGY.items():
            if v not in DEAD and v_energy >= LIMIT:
                DEAD.add(v)
                for y in E[v]:
                    if y in NEW_AMTS:
                        if 10 in NEW_AMTS[y]:
                            NEW_AMTS[y][10] += 1
                        else:
                            NEW_AMTS[y][10] = 1
                    else:
                        NEW_AMTS[y] = {10: 1}
        AMTS = NEW_AMTS
        if len(AMTS) == 0:
            break
    ret = 0
    for v,v_energy in ENERGY.items():
        if v not in DEAD:
            assert v_energy < LIMIT
            ret += v_energy
    return ret

ans = None
for v in E:
    #if v != 74:
    #    continue
    score = total_energy(deepcopy(ENERGY), E, v)
    if ans is None or score > ans:
        ans = score
    print(f'{v=} {score=} {ans=}')
print(ans)
