import sys
import heapq
from collections import deque
from copy import deepcopy

SCORE = {}
THICKNESS = {}
D = sys.stdin.read()
plants, cases = D.split('\n\n\n')
rows = plants.split('\n\n')

ans = 0
for case in cases.splitlines():
    xs = [int(x) for x in case.split()]
    xi = 0

    for i,row in enumerate(rows):
        lines = row.splitlines()
        words = lines[0].split()
        id_ = int(words[1])
        thickness = int(words[-1][:-1])
        THICKNESS[id_] = thickness
        SCORE[id_] = 0
        for line in lines[1:]:
            words = line.split()
            if words[1]=='free':
                SCORE[id_] += xs[xi]
                xi += 1
            else:
                child_id = int(words[4])
                child_thickness = int(words[-1])
                print(f'{id_=} {child_id=} {child_thickness=} {SCORE[child_id]=}')
                SCORE[id_] += SCORE[child_id]*child_thickness
        if SCORE[id_] < THICKNESS[id_]:
            SCORE[id_] = 0
        if i==len(rows)-1:
            ans += SCORE[id_]
print(ans)
