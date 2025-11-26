import sys
import heapq
import itertools
from collections import deque
from copy import deepcopy
import sympy

SCORE = {}
D = sys.stdin.read()
plants, cases = D.split('\n\n\n')
rows = plants.split('\n\n')

PLANTS = {}
THICKNESS = {}
last = None
for i,row in enumerate(rows):
    lines = row.splitlines()
    words = lines[0].split()
    id_ = int(words[1])
    thickness = int(words[-1][:-1])
    THICKNESS[id_] = thickness
    for line in lines[1:]:
        words = line.split()
        if words[1]=='free':
            PLANTS[id_] = 'FREE'
        else:
            child_id = int(words[4])
            child_thickness = int(words[-1])
            if id_ not in PLANTS:
                PLANTS[id_] = []
            PLANTS[id_].append((child_id, child_thickness))
    last = id_

FREE = {p for p,v in PLANTS.items() if v=='FREE'}
GOOD = set()
BAD = set()
for k,v in PLANTS.items():
    if v!='FREE':
        for k2,v2 in v:
            if v2>0:
                GOOD.add(k2)
                assert k2 not in BAD
            else:
                BAD.add(k2)
                assert k2 not in GOOD

best = 0
SCORE = {}
for k,v in PLANTS.items():
    if v=='FREE':
        SCORE[k] = (1 if k in GOOD else 0)
    else:
        SCORE[k] = 0
        for k2,v2 in v:
            SCORE[k] += SCORE[k2]*v2
        if SCORE[k] < THICKNESS[k]:
            SCORE[k] = 0
best = SCORE[last]

ans = 0
for case in cases.splitlines():
    xs = [int(x) for x in case.split()]
    xi = 0

    SCORE = {}
    for k,v in PLANTS.items():
        if v=='FREE':
            SCORE[k] = xs[xi]
            xi += 1
        else:
            SCORE[k] = 0
            for k2,v2 in v:
                SCORE[k] += SCORE[k2]*v2
            if SCORE[k] < THICKNESS[k]:
                SCORE[k] = 0
    if SCORE[last] > 0:
        ans += best-SCORE[last]
print(ans)
